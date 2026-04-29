 
def parse_github_url(url):
    """
    Extract the owner and repo name from a GitHub URL.
   
   example:
   https://github.com/user/repo → owner: user, repo: repo
       
   
    """
    parts=url.split("/")
    if(len(parts)<5):
        raise ValueError("Invalid GitHub URL. Expected format:")
                         
    owner=parts[3]
    repo=parts[4].replace(".git","")
    
    return owner, repo