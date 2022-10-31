"""
Class: Profile

Description:

    Contains all information about the course being parsed. The source folder 
    should be the base folder of the project and conform to the Obsidian 
    format. 

Methods:
    get_sections
    get_section_pages
    get_page_paths

Issues:
    - Currently only works with one level under each section, so nested
      folders will not be included.
      - RESOLVED: Should be fixed at this point
     
    
    - Assets folder not yet included.
      - RESOLVED: Assets included as assets_paths

"""
import os
from pathlib import Path


class SiteProfile:
    def __init__(self, source):
        """
        Parameters:
            source: base folder of the project
        """
        self.source = source
        self.sections = self.get_sections()
        self.asset_paths = self.get_assets_paths()

    def get_sections(self):
        """
        Gets all folders which are not the asset folder. These files should
        contain markdown to be rendered.
        """
        try:
            root = Path(self.source)
            sections = {"root": []}
            for path in Path(root).rglob("*"):
                if not self.is_valid_path(path):
                    continue
                if os.path.isfile(path):
                    if path.parent in sections:
                        sections[path.parent].append(path)
                    else:
                        sections[path.parent] = [path]
            return sections

        except Exception as e:
            print("[get_sections]", e)

    def is_valid_path(self, path):
        """
        Checks if the path is valid. A path is valid if it's:

            1. Not in the assets or .obsidian folders.
            2. Is a markdown file.
        """
        excluded = [
            os.path.join(self.source, exclude) for exclude in ["assets", ".obsidian"]
        ]
        for exclude in excluded:
            if str(path).startswith(str(exclude)):
                return False
        if Path(path).suffix.lower() == ".md":
            return True
        return False

    def get_assets_paths(self):
        """
        Gets the assets paths as key with the filename name as value.

        Issues: Use os walk to get full tree and scan that way.
        """
        try:
            asset_paths = {}
            path = os.path.join(self.source, "assets")
            for asset_path in Path(path).rglob("*"):
                asset = os.path.relpath(asset_path, path)
                if os.path.isfile(asset_path):
                    asset_paths[str(asset_path)] = asset
            return asset_paths

        except Exception as e:
            print("[get_assets_paths]", e)


if __name__ == "__main__":
    course_profile = SiteProfile("../course")
    print("\nSections ------------")
    print(course_profile.sections)

    print("\nAssests Paths ------------")
    print(course_profile.asset_paths)
