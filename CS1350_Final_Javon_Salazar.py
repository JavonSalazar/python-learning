#Javon Salazar

#Problem 2 - Skill Matcher 
def skill_analysis(candidates, required):
    fully_qualified = []
    best_match = None
    best_count = -1

    for name, skills in candidates.items():
        if required <= skills:
            fully_qualified.append(name)

        match_count = len(skills & required)
        if match_count > best_count or (match_count == best_count and (best_match is None or name < best_match)):
            best_count = match_count
            best_match = name
    fully_qualified.sort()

    all_skills = {}
    for name, skills in candidates.items():
        for skill in skills:
            all_skills[skill] = all_skills.get(skill, 0) + 1

    unique_skills = {}
    for name, skills in candidates.items():
        unique = sorted([s for s in skills if all_skills[s] == 1])
        if unique:
            unique_skills[name] = unique

    return {
        "fully_qualified": fully_qualified,
        "best_match": best_match,
        "unique_skills": unique_skills
    }
   
    
#Problem 3 - Regex Parser
import re

HASHTAG_RE = re.compile(r"#(\w+)")
MENTION_RE = re.compile(r"@(\w+)")
URL_RE = re.compile(r"https?://\S+")

def remove_duplicates_preserve_order(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def parse_post(text):
    hashtags = remove_duplicates_preserve_order(HASHTAG_RE.findall(text))
    mentions = remove_duplicates_preserve_order(MENTION_RE.findall(text))
    urls = remove_duplicates_preserve_order(URL_RE.findall(text))

    return {
        "hashtags": hashtags,
        "mentions": mentions,
        "urls": urls
    }


#Problem 5 - Subset Sum
def subset_sum(nums, target):
    if target == 0:
        return True
    if not nums:
        return False

    return (
        subset_sum(nums[1:], target - nums[0]) or
        subset_sum(nums[1:], target)
    )
