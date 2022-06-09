# -*- coding:utf-8 -*-
from typing import List
from collections import Counter


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = Counter()

        for cpdomain in cpdomains:
            cnt, domain = cpdomain.split(" ")
            cnt = int(cnt)
            split_domains = domain.split(".")
            for i in range(len(split_domains)):
                ans[".".join(split_domains[i:])] += cnt
        
        return ["{} {}".format(cnt, dom) for dom, cnt in ans.items()]


class TestSubdomainVists:

    """
    pytest -s 811_subdomain_visit_count.py::TestSubdomainVists
    """

    def test(self):
        solution = Solution()

        cpdomains = ["9001 discuss.leetcode.com"]
        assert ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"] == solution.subdomainVisits(cpdomains)

        cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
        assert ['900 google.mail.com', '901 mail.com', '951 com', '50 yahoo.com', '1 intel.mail.com', '5 wiki.org', '5 org'] == solution.subdomainVisits(cpdomains)

