"""Inspect APIs
"""

import operator
import unittest

import requests

from .config import *
from .techstacks_dtos import *


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GithubRepo:
    name: str
    description: Optional[str] = None
    homepage: Optional[str] = None
    lang: Optional[str] = field(metadata=config(field_name="language"), default=None)
    watchers: Optional[int] = 0
    forks: Optional[int] = 0


class TestTechStacks(unittest.TestCase):

    def test_does_dump(self):
        org_name = "python"
        response = requests.get(f'https://api.github.com/orgs/{org_name}/repos')
        org_repos = GithubRepo.schema().loads(response.text, many=True)
        org_repos.sort(key=operator.attrgetter('watchers'), reverse=True)

        print(f'Top 3 {org_name} Repos:')
        printdump(org_repos[0:3])

        print(f'\nTop 10 {org_name} Repos:')
        printtable(org_repos[0:10], headers=['name', 'lang', 'watchers', 'forks'])

        inspect_vars({'org_repos': org_repos})

    def test_does_support_FindTechnologies(self):
        client = create_techstacks_client()
        response = client.send(FindTechnologies(
            ids=[1, 2, 3],
            vendor_name="Google",
            take=5,
            fields='id,name,vendorName,createdBy,viewCount,favCount'))

        printdump(response)
        printtable(response.results)
        printtable(response.results,
                   headers=['id', 'name', 'vendor_name', 'view_count', 'fav_count'])
        printtable(response.results,
                   headers=['Id', 'Name', 'VendorName', 'ViewCount', 'FavCount'])
        printtable(to_dict(response.results, key_case=titlecase))
        printhtmldump(response)
        inspect_vars({"response": response})
