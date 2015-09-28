import glob

from lyx_sections.generate_generic_templates import inset_template, templates
from lyx_sections.misc_utils import UserError
from lyx_sections.subst import substitute

from . import logger
from lyx_sections.natsorting import natsorted
from contracts import contract


def generate(pattern, entry2value,
                           template_main=templates['amsbook'],
                           template_inset=inset_template,
                           exclude=[]):

    main = generate_index(pattern, entry2value,
                          template_main,
                          template_inset,
                          exclude)
    print(main)


@contract(pattern='str|None', extra_files='list(str)')
def generate_index(pattern, extra_files, entry2value,
                           template_main=templates['amsbook'],
                           template_inset=inset_template,
                           exclude=[],
                           preamble=''):
    chapters = []

    if pattern is not None:
        cs = list(glob.glob(pattern))

        if not cs:
            msg = 'Could not find any file matching %r.' % pattern
            raise UserError(msg)

        chapters.extend(cs)

    chapters.extend(extra_files)

    for e in exclude:
        if e in chapters:
            logger.debug('Removing %s' % e)
            chapters.remove(e)


    s = "\n".join("  - %3d: %s" % (i + 1, c)  for i, c in enumerate(chapters))
    logger.info('Found:\n%s ' % s)

    chapters = natsorted(chapters)
    main = create_lyx_file(chapters, entry2value, template_main, template_inset,
                           preamble=preamble)
    logger.debug('Done.')
    return main

def create_lyx_file(chapters, entry2value, template_main, template_inset,
                    preamble=''):
    """ Returns a string with the template """
    insets = ''
    for chap in chapters:
        filename = entry2value(chap) 
        inset = substitute(template_inset, filename=filename)
        insets += inset 

    main = substitute(template_main, content=insets, preamble=preamble)
    return main


