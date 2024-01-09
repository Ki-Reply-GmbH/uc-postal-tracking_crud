1. Resolved merge conflict in file: app/models.py:
```python
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
```
Explanation: The conflict occurred because both branches modified the same section of code. The changes in the `base repo` branch were adding an import for `DateTime` and `datetime`, while the `target repo` branch added an import for `Integer`. We have resolved the conflict by including all the unique imports from both branches.

2. Message for the Pull request:
```markdown
Merged changes from the base repo to add Authentication feature. 

The merge conflict in `app/models.py` was resolved by combining the unique imports from both branches. This ensures that we preserve all existing functionality in the target repository while also adding the new Authentication feature.

Please review the changes and let me know if there are any concerns.
```

3. Task list for git commands as JSON object:
```json
{
    "1": "git checkout target_branch",
    "2": "git pull origin target_branch",
    "3": "git merge base_repo_branch",
    "4": "Resolve merge conflicts manually",
    "5": "git add app/models.py",
    "6": "git commit -m 'Merged base_repo_branch to add Authentication feature'",
    "7": "git push origin target_branch"
}
```
Explanation: These commands are for switching to the target branch, updating it to its latest state, merging the base repo branch into it, resolving merge conflicts manually, committing the changes and pushing them to the remote repository.