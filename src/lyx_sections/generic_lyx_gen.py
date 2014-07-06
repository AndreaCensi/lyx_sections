from optparse import OptionParser
import os

from .generate_generic import generate_index
from .generate_generic_templates import templates
from .misc_utils import UserError
from .misc_utils import wrap_script


def lyx_gen(args):

    parser = OptionParser()
    
    parser.add_option("-o", "--output", help="Output file")

    parser.add_option("-c", "--textclass", default='amsbook',
                      help="LyX text class")

    parser.add_option("-p", "--pattern", help="File pattern",
                      default='*.lyx')
    
    parser.add_option("-P", "--preamble", help="Preamble section", default='')
    
    params = args[1:]

    if not params:
        name = os.path.basename(args[0])
        print('Usage:\n\t%s  -c [ %s ]'
              '\n\t\t -p "<name>_*.lyx"\n\t\t -o <output>.lyx'
              % (name, ' | '.join(templates.keys())))

    options, which = parser.parse_args(params)
    
    if not options.output:
        msg = 'Please provide output argument with -o.'
        raise UserError(msg)
            
    if which:
        msg = 'Spurious arguments: %s' % which
        raise UserError(msg)


    template_main = templates[options.textclass]
    
    main = generate_index(
        pattern=options.pattern,
        template_main=template_main,
        entry2value=lambda x: '%s' % x,
        exclude=['chapter.lyx', 'chapter0.lyx', 'chapter_contents.lyx'],
        preamble=options.preamble)
    
    with open(options.output, 'wb') as f:
        f.write(main)

def lyx_gen_main():
    wrap_script(lyx_gen)
