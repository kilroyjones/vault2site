"""
Main
"""

import markdown as md
from builder import Builder
from profile import Profile
from processors.links import Links
from processors.images import Images
from processors.quizzes import Quizzes
from processors.sidenotes import Sidenotes

if __name__ == "__main__":
    import os

    course_profile = Profile(
        "/home/kilroy/code/projects/course_builder/markdown_editor/app/course",
    )
    course_builder = Builder(course_profile, md, [Quizzes, Links])
    course_builder.output_markdown(
        "/home/kilroy/code/projects/course_builder/markdown_editor/app/svelte-site"
    )
