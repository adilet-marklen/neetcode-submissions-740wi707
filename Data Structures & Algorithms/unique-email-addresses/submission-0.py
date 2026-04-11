class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashmap = {}

        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '')
            if '+' in local:
                local = local[:local.index('+')]
            adress = local + domain
            hashmap[adress] = hashmap.get(adress, 0) + 1
        
        return len(hashmap.values())