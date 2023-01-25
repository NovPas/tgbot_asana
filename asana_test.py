import os
import asana

# Note: Replace this value with your own personal access token
personal_access_token_asana = "1/1203489910254785:ab0204bf2da01b02a1dc8db6058e521f"

# Construct an Asana client
client = asana.Client.access_token(personal_access_token_asana)

# Get your user info
me = client.users.me()
print(me['name'])
workspace_id = me['workspaces'][0]['gid']

tasks = client.tasks.find_all(workspace=workspace_id, completed_since='now', assignee=me['gid'])

ls = []

for t in tasks:
    ls.append(t['name'])

result = '\n'.join(ls)

print(result)


# asana.resources.tasks.Tasks.get_tasks_for_user_task_list(user_task_list_gid=me['gid'])

# tasks = client.tasks.get_tasks({'workspace': workspace_id}, page_size=100)
#         client.
# tasks = client.user_task_lists.get_user_task_list_for_user(me['gid'], , opt_pretty=True)
