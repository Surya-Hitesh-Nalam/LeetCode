class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans=[]
        for fold in folder:
            if not ans:
                ans.append(fold)
            else:
                if fold.startswith(ans[-1]) and len(fold)>len(ans[-1]) and fold[len(ans[-1])]=="/":
                    continue
                else:
                    ans.append(fold)
        return ans
        