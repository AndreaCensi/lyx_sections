from setuptools import setup, find_packages

setup(name='LyxSections',
        author="Andrea Censi",
        author_email="censi@mit.edu",
        version="0.5",
        package_dir={'':'src'},
        packages=find_packages('src'),
        entry_points={
         'console_scripts': [
           # Summaries
           'lyx-gen-chapter = lyx_sections:generate_chapter_contents_main',
           'lyx-gen-part  = lyx_sections:generate_part_contents_main',
           'lyx-gen  = lyx_sections:lyx_gen_main',
           ]
        },
        install_requires=[],
        extras_require={},
)

