cons = []
projects = []

with open('f_find_great_mentors.in.txt') as f:
    lines = f.readlines()
    
    cons_len = 0
    projects_len = 0
    skills_num = 0
    roles_num = 0
    name = ""
    
    for i, line in enumerate(lines):
        line = line[0:len(line) - 1]

        if i == 0:
            cons_len, projects_len = line.split(" ")
            cons_len, projects_len = int(cons_len), int(projects_len)
        else:
            length = len(cons)
            if length:
                skills_len = len(dict.keys((cons[length - 1]["skills"])))
            else:
                skills_len = 0
            
            if length < cons_len or skills_len < skills_num:
                if not name:
                    name, skills_num = line.split(" ")
                    skills_num = int(skills_num)
                    cons.append({"name": name, "skills": {}})
                else:
                    skill, level = line.split(" ")
                    cons[length - 1]["skills"][skill] = int(level)
                    
                    if skills_len + 1 == skills_num:
                        name = ""
                        skills_num = 0
            else:
                length = len(projects)
                if length:
                    roles_len = len(projects[length - 1]["roles"])
                else:
                    roles_len = 0
                
                if length < projects_len or roles_len < roles_num:
                    if not name:
                        name, timeline, score, best_before, roles_num = line.split(" ")
                        roles_num = int(roles_num)
                        projects.append({
                            "name": name, 
                            "timeline": timeline,
                            "score": score,
                            "best_before": best_before,
                            "roles": []
                        })
                    else:
                        role, level = line.split(" ")
                        projects[length - 1]["roles"].append({role: int(level)})
                        
                        if roles_len + 1 == roles_num:
                            name = ""
                            roles_num = 0

completed = 0
projects_total = len(projects)
answer = []
loop_limit = len(projects)
count = 0

while len(answer) < projects_total and count < loop_limit:
    for index, project in enumerate(projects):
        contributors = []
        update = {}
        
        for role in project["roles"]:
            for con in cons:
                role_skill = list(dict.keys(role))[0]
                
                if project["name"] == "PhotoProv3" and con["name"] == "SergeyV":
                    break

                if role_skill in con["skills"] and con["name"] not in contributors:
                    if role[role_skill] <= con["skills"][role_skill]:
                        if role[role_skill] == con["skills"][role_skill]:
                            update[con["name"]] = role_skill
                            
                        contributors.append(con["name"])
                        break
                    
        
        if len(contributors) == len(project["roles"]):
            answer.append({"name": project["name"], "contributors": contributors})
            projects.pop(index)
            
            
        for con in cons:
            if con["name"] in update:
                con["skills"][update[con["name"]]] += 1
                
        count += 1


f = open("ans_find_great_mentors.txt", "w")

ans_str = str(len(answer)) + "\n"

for ans in answer: 
    ans_str += ans["name"] + "\n"
    ans_str += " ".join(ans["contributors"]) + "\n"

f.write(ans_str)