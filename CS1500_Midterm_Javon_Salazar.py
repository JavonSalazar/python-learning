#problem 1

class Inventory:
    def __init__(self):
        self.products = {}  

    def add_product(self, name, price, quantity):
        if name in self.products:
            self.products[name]["quantity"] += quantity
            self.products[name]["price"] = price 
        else:
            self.products[name] = {"price": price, "quantity": quantity}

    def sell(self, name, amount):
        if name not in self.products:
            raise ValueError(f"Product '{name}' not found.")
        if self.products[name]["quantity"] < amount:
            raise ValueError(f"Insufficient stock for '{name}'.")
        self.products[name]["quantity"] -= amount

    def restock_report(self):
        return sorted([name for name, data in self.products.items() if data["quantity"] < 5])

    def total_value(self):
        return sum(d["price"] * d["quantity"] for d in self.products.values())

    def most_valuable(self):
        if not self.products: return None
        return max(self.products, key=lambda name: self.products[name]["price"] * self.products[name]["quantity"])

#problem 2

class Team:
    def __init__(self, name, players=None):
        self.name = name
        self.players = set(players) if players else set()

    def add_player(self, name):
        self.players.add(name)

    def remove_player(self, name):
        self.players.discard(name) 
        
    def roster_size(self):
        return len(self.players)

def shared_players(team1, team2):
    return team1.players & team2.players 

def all_players(teams):
    total_roster = set()
    for t in teams:
        total_roster |= t.players 
    return total_roster

def find_duplicates(teams):
    player_map = {}
    for t in teams:
        for p in t.players:
            player_map.setdefault(p, []).append(t.name)
    
    return {p: sorted(teams) for p, teams in player_map.items() if len(teams) > 1}

def eligible_allstars(teams, min_teams):
    counts = {}
    for t in teams:
        for p in t.players:
            counts[p] = counts.get(p, 0) + 1
    return {p for p, count in counts.items() if count >= min_teams}

#problem 3

import numpy as np

class ImageProcessor:
    def __init__(self, image_array):
        self.image = np.array(image_array)

    def crop(self, y1, y2, x1, x2):
        return self.image[y1:y2, x1:x2]

    def adjust_brightness(self, factor):
        adjusted = self.image * factor
        return np.clip(adjusted, 0, 255).astype(np.uint8)

    def get_channel_stats(self):
        return {
            "mean": np.mean(self.image, axis=(0, 1)),
            "std": np.std(self.image, axis=(0, 1))
        }

    def apply_mask(self, mask):
        result = self.image.copy()
        result[~mask] = 0
        return result

#problem 4

from abc import ABC, abstractmethod

class Media(ABC):
    def __init__(self, title, creator, id_code):
        self.title = title
        self.creator = creator
        self.id_code = id_code
        self.is_checked_out = False

    @abstractmethod
    def calculate_fine(self, days_overdue):
        """Must be implemented by subclasses."""
        pass

class Book(Media):
    def calculate_fine(self, days_overdue):
        return max(0, days_overdue * 0.50)

class Magazine(Media):
    def calculate_fine(self, days_overdue):
        return max(0, days_overdue * 1.00)

class Library:
    def __init__(self):
        self.catalog = {}
    def add_media(self, item):
        self.catalog[item.id_code] = item

    def check_out(self, id_code):
        if id_code in self.catalog and not self.catalog[id_code].is_checked_out:
            self.catalog[id_code].is_checked_out = True
            return True
        return False

    def total_potential_fines(self, overdue_data):
        total = 0.0
        for id_code, days in overdue_data:
            if id_code in self.catalog:
                total += self.catalog[id_code].calculate_fine(days)
        return total

#problem 5

import numpy as np
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Polygon(Shape):
    def __init__(self, vertices):
        self.vertices = np.array(vertices)

    def perimeter(self):
        diff = self.vertices - np.roll(self.vertices, shift=-1, axis=0)
        distances = np.sqrt(np.sum(diff**2, axis=1))
        return np.sum(distances)

    def area(self):
        x = self.vertices[:, 0]
        y = self.vertices[:, 1]
        return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

def find_largest_area(shapes):
    if not shapes:
        return None
    return max(shapes, key=lambda s: s.area())

