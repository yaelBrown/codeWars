"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
"""
def domain_name(url):
  url = url.replace("http://", "")
  url = url.replace("https://", "")
  url = url.replace("www.", "")
  sep = url.index(".")
  return url[0:sep]
  
domain_name("http://www.google.com")

"""
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')
import re
def domain_name(url):
    return re.search("(//|www.)(\w+)[.]", url).group(2)
def domain_name(url):
    
   if ("www" not in url): return url.split("//")[1].split(".")[0]
   else: return url.split(".")[1]
"""