from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        site_count = defaultdict(int)
        
        for i in cpdomains:
            count, site = i.split()
            count = int(count)
            
            site_count[site] += count
            domains = site.split(".", 1)
            while(len(domains)>1):
                site = domains[1]
                site_count[site] += count
                domains = site.split(".", 1)
                
        counts = [f"{site_count[i]} {i}" for i in site_count]
        return counts
                
        