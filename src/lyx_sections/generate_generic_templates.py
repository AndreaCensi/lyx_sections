
inset_template = r"""
\begin_layout Standard
\begin_inset CommandInset include
LatexCommand input
filename "${filename}"

\end_inset


\end_layout
"""

templates = {}
templates['amsbook'] = r"""#LyX 2.0 created this file. For more info see http://www.lyx.org/
\lyxformat 413
\begin_document
\begin_header
\textclass amsbook
\begin_preamble
${preamble}
\end_preamble
\options onecolumn
\use_default_options true
\begin_modules
theorems-ams-bytype
eqs-within-sections
figs-within-sections
\end_modules
\maintain_unincluded_children false
\language english
\language_package default
\inputencoding auto
\fontencoding global
\font_roman palatino
\font_sans default
\font_typewriter default
\font_default_family default
\use_non_tex_fonts false
\font_sc false
\font_osf false
\font_sf_scale 100
\font_tt_scale 100

\graphics default
\default_output_format default
\output_sync 0
\bibtex_command default
\index_command default
\paperfontsize default
\spacing single
\use_hyperref false
\pdf_bookmarks true
\pdf_bookmarksnumbered false
\pdf_bookmarksopen false
\pdf_bookmarksopenlevel 1
\pdf_breaklinks true
\pdf_pdfborder true
\pdf_colorlinks true
\pdf_backref page
\pdf_pdfusetitle true
\papersize default
\use_geometry false
\use_amsmath 1
\use_esint 1
\use_mhchem 1
\use_mathdots 1
\cite_engine basic
\use_bibtopic false
\use_indices false
\paperorientation portrait
\suppress_date true
\use_refstyle 0
\branch report
\selected 0
\filename_suffix 0
\color #000000
\end_branch
\branch conf
\selected 0
\filename_suffix 0
\color #000000
\end_branch
\branch AC
\selected 1
\filename_suffix 0
\color #682743
\end_branch
\index Index
\shortcut idx
\color #008000
\end_index
\secnumdepth 3
\tocdepth 3
\paragraph_separation indent
\paragraph_indentation default
\quotes_language english
\papercolumns 1
\papersides 1
\paperpagestyle default
\tracking_changes false
\output_changes false
\html_math_output 0
\html_css_as_file 0
\html_be_strict false
\end_header

\begin_body

${content}

\end_body
\end_document
"""
# TODO: get rid of tex/preamble

templates['IEEEtran'] = r"""#LyX 2.0 created this file. For more info see http://www.lyx.org/
\lyxformat 413
\begin_document
\begin_header
\textclass IEEEtran
\begin_preamble
${preamble}
\end_preamble
\use_default_options true
\begin_modules
theorems-ams-bytype
\end_modules
\maintain_unincluded_children false
\language english
\language_package default
\inputencoding auto
\fontencoding global
\font_roman default
\font_sans default
\font_typewriter default
\font_default_family default
\use_non_tex_fonts false
\font_sc false
\font_osf false
\font_sf_scale 100
\font_tt_scale 100

\graphics default
\default_output_format default
\output_sync 0
\bibtex_command default
\index_command default
\paperfontsize default
\spacing single
\use_hyperref false
\pdf_bookmarks true
\pdf_bookmarksnumbered false
\pdf_bookmarksopen false
\pdf_bookmarksopenlevel 1
\pdf_breaklinks true
\pdf_pdfborder true
\pdf_colorlinks true
\pdf_backref page
\pdf_pdfusetitle true
\papersize default
\use_geometry false
\use_amsmath 1
\use_esint 1
\use_mhchem 1
\use_mathdots 1
\cite_engine basic
\use_bibtopic false
\use_indices false
\paperorientation portrait
\suppress_date true
\use_refstyle 0
\branch report
\selected 0
\filename_suffix 0
\color #000000
\end_branch
\branch conf
\selected 1
\filename_suffix 0
\color #000000
\end_branch
\branch journal
\selected 0
\filename_suffix 0
\color #000000
\end_branch
\branch AC
\selected 1
\filename_suffix 0
\color #682743
\end_branch
\index Index
\shortcut idx
\color #008000
\end_index
\secnumdepth 3
\tocdepth 3
\paragraph_separation indent
\paragraph_indentation default
\quotes_language english
\papercolumns 2
\papersides 1
\paperpagestyle default
\tracking_changes false
\output_changes false
\html_math_output 0
\html_css_as_file 0
\html_be_strict false
\end_header

\begin_body

${content}

\end_body
\end_document
"""

templates['IEEEtran1col'] = r"""#LyX 2.0 created this file. For more info see http://www.lyx.org/
\lyxformat 413
\begin_document
\begin_header
\textclass IEEEtran
\begin_preamble
${preamble}
\end_preamble
\options onecolumn
\use_default_options true
\begin_modules
theorems-ams-bytype
\end_modules
\maintain_unincluded_children false
\language english
\language_package default
\inputencoding auto
\fontencoding global
\font_roman default
\font_sans default
\font_typewriter default
\font_default_family default
\use_non_tex_fonts false
\font_sc false
\font_osf false
\font_sf_scale 100
\font_tt_scale 100

\graphics default
\default_output_format default
\output_sync 0
\bibtex_command default
\index_command default
\paperfontsize default
\spacing single
\use_hyperref false
\pdf_bookmarks true
\pdf_bookmarksnumbered false
\pdf_bookmarksopen false
\pdf_bookmarksopenlevel 1
\pdf_breaklinks true
\pdf_pdfborder true
\pdf_colorlinks true
\pdf_backref page
\pdf_pdfusetitle true
\papersize default
\use_geometry false
\use_amsmath 1
\use_esint 1
\use_mhchem 1
\use_mathdots 1
\cite_engine basic
\use_bibtopic false
\use_indices false
\paperorientation portrait
\suppress_date true
\use_refstyle 0
\branch report
\selected 0
\filename_suffix 0
\color #000000
\end_branch
\branch journal
\selected 1
\filename_suffix 0
\color #000000
\end_branch
\branch conf
\selected 0
\filename_suffix 0
\color #000000
\end_branch
\branch AC
\selected 1
\filename_suffix 0
\color #682743
\end_branch
\index Index
\shortcut idx
\color #008000
\end_index
\secnumdepth 3
\tocdepth 3
\paragraph_separation indent
\paragraph_indentation default
\quotes_language english
\papercolumns 1
\papersides 1
\paperpagestyle default
\tracking_changes false
\output_changes false
\html_math_output 0
\html_css_as_file 0
\html_be_strict false
\end_header

\begin_body

${content}

\end_body
\end_document
"""


templates['IEEEconf'] = r"""#LyX 2.0 created this file. For more info see http://www.lyx.org/
\lyxformat 413
\begin_document
\begin_header
\textclass IEEEconf
\begin_preamble
${preamble}
\end_preamble
\options letterpaper,conference,10pt
\use_default_options true
\begin_modules
theorems-ams-bytype
\end_modules
\maintain_unincluded_children false
\language english
\language_package default
\inputencoding auto
\fontencoding global
\font_roman default
\font_sans default
\font_typewriter default
\font_default_family default
\use_non_tex_fonts false
\font_sc false
\font_osf false
\font_sf_scale 100
\font_tt_scale 100

\graphics default
\default_output_format default
\output_sync 0
\bibtex_command default
\index_command default
\paperfontsize default
\spacing single
\use_hyperref false
\pdf_bookmarks true
\pdf_bookmarksnumbered false
\pdf_bookmarksopen false
\pdf_bookmarksopenlevel 1
\pdf_breaklinks true
\pdf_pdfborder true
\pdf_colorlinks true
\pdf_backref page
\pdf_pdfusetitle true
\papersize default
\use_geometry false
\use_amsmath 1
\use_esint 1
\use_mhchem 1
\use_mathdots 1
\cite_engine basic
\use_bibtopic false
\use_indices false
\paperorientation portrait
\suppress_date true
\use_refstyle 1
\branch report
\selected 0
\filename_suffix 0
\color #000000
\end_branch
\branch journal
\selected 0
\filename_suffix 0
\color #000000
\end_branch
\branch conf
\selected 1
\filename_suffix 0
\color #000000
\end_branch
\branch AC
\selected 1
\filename_suffix 0
\color #682743
\end_branch
\index Index
\shortcut idx
\color #008000
\end_index
\secnumdepth 3
\tocdepth 3
\paragraph_separation indent
\paragraph_indentation default
\quotes_language english
\papercolumns 2
\papersides 1
\paperpagestyle default
\tracking_changes false
\output_changes false
\html_math_output 0
\html_css_as_file 0
\html_be_strict false
\end_header

\begin_body

${content}

\end_body
\end_document
"""

templates['article'] = r"""#LyX 2.0 created this file. For more info see http://www.lyx.org/
\lyxformat 413
\begin_document
\begin_header
\textclass article
\begin_preamble
${preamble}
\end_preamble
\options onecolumn
\use_default_options true
\begin_modules
theorems-ams-bytype
\end_modules
\maintain_unincluded_children false
\language english
\language_package default
\inputencoding auto
\fontencoding global
\font_roman default
\font_sans default
\font_typewriter default
\font_default_family default
\use_non_tex_fonts false
\font_sc false
\font_osf false
\font_sf_scale 100
\font_tt_scale 100

\graphics default
\default_output_format default
\output_sync 0
\bibtex_command default
\index_command default
\paperfontsize default
\spacing single
\use_hyperref false
\pdf_bookmarks true
\pdf_bookmarksnumbered false
\pdf_bookmarksopen false
\pdf_bookmarksopenlevel 1
\pdf_breaklinks true
\pdf_pdfborder true
\pdf_colorlinks true
\pdf_backref page
\pdf_pdfusetitle true
\papersize default
\use_geometry false
\use_amsmath 1
\use_esint 1
\use_mhchem 1
\use_mathdots 1
\cite_engine basic
\use_bibtopic false
\use_indices false
\paperorientation portrait
\suppress_date true
\use_refstyle 0
\branch report
\selected 0
\filename_suffix 0
\color #000000
\end_branch
\branch conf
\selected 0
\filename_suffix 0
\color #000000
\end_branch
\branch AC
\selected 1
\filename_suffix 0
\color #682743
\end_branch
\index Index
\shortcut idx
\color #008000
\end_index
\secnumdepth 3
\tocdepth 3
\paragraph_separation indent
\paragraph_indentation default
\quotes_language english
\papercolumns 1
\papersides 1
\paperpagestyle default
\tracking_changes false
\output_changes false
\html_math_output 0
\html_css_as_file 0
\html_be_strict false
\end_header

\begin_body

${content}

\end_body
\end_document
"""


templates['article11'] = r"""#LyX 2.0 created this file. For more info see http://www.lyx.org/
\lyxformat 413
\begin_document
\begin_header
\textclass article
\begin_preamble
${preamble}
\end_preamble
\options onecolumn
\use_default_options true
\begin_modules
theorems-ams-bytype
\end_modules
\maintain_unincluded_children false
\language english
\language_package default
\inputencoding auto
\fontencoding global
\font_roman default
\font_sans default
\font_typewriter default
\font_default_family default
\use_non_tex_fonts false
\font_sc false
\font_osf false
\font_sf_scale 100
\font_tt_scale 100

\graphics default
\default_output_format default
\output_sync 0
\bibtex_command default
\index_command default
\paperfontsize 11
\spacing single
\use_hyperref false
\pdf_bookmarks true
\pdf_bookmarksnumbered false
\pdf_bookmarksopen false
\pdf_bookmarksopenlevel 1
\pdf_breaklinks true
\pdf_pdfborder true
\pdf_colorlinks true
\pdf_backref page
\pdf_pdfusetitle true
\papersize default
\use_geometry false
\use_amsmath 1
\use_esint 1
\use_mhchem 1
\use_mathdots 1
\cite_engine basic
\use_bibtopic false
\use_indices false
\paperorientation portrait
\suppress_date true
\use_refstyle 0
\branch report
\selected 0
\filename_suffix 0
\color #000000
\end_branch
\branch conf
\selected 0
\filename_suffix 0
\color #000000
\end_branch
\branch AC
\selected 1
\filename_suffix 0
\color #682743
\end_branch
\index Index
\shortcut idx
\color #008000
\end_index
\secnumdepth 3
\tocdepth 3
\paragraph_separation indent
\paragraph_indentation default
\quotes_language english
\papercolumns 1
\papersides 1
\paperpagestyle default
\tracking_changes false
\output_changes false
\html_math_output 0
\html_css_as_file 0
\html_be_strict false
\end_header

\begin_body

${content}

\end_body
\end_document
"""

# fixltx2e => unknown pacakge H

templates['IEEEtrantn'] = r"""
#LyX 2.1 created this file. For more info see http://www.lyx.org/
\lyxformat 474
\begin_document
\begin_header
\textclass IEEEtran
\options technote
\begin_preamble
${preamble}
\end_preamble
\use_default_options true
\begin_modules
\end_modules
\maintain_unincluded_children false
\language english
\language_package default
\inputencoding auto
\fontencoding global
\font_roman default
\font_sans default
\font_typewriter default
\font_math auto
\font_default_family default
\use_non_tex_fonts false
\font_sc false
\font_osf false
\font_sf_scale 100
\font_tt_scale 100
\graphics default
\default_output_format default
\output_sync 0
\bibtex_command default
\index_command default
\paperfontsize 9
\spacing single
\use_hyperref false
\papersize default
\use_geometry false
\use_package amsmath 1
\use_package amssymb 1
\use_package cancel 1
\use_package esint 1
\use_package mathdots 1
\use_package mathtools 1
\use_package mhchem 1
\use_package stackrel 1
\use_package stmaryrd 1
\use_package undertilde 1
\cite_engine basic
\cite_engine_type default
\biblio_style plain
\use_bibtopic false
\use_indices false
\paperorientation portrait
\suppress_date false
\justification true
\use_refstyle 0
\index Index
\shortcut idx
\color #008000
\end_index
\secnumdepth 3
\tocdepth 3
\paragraph_separation indent
\paragraph_indentation default
\quotes_language english
\papercolumns 1
\papersides 1
\paperpagestyle default
\tracking_changes false
\output_changes false
\html_math_output 0
\html_css_as_file 0
\html_be_strict false
\end_header

\begin_body

${content}

\end_body
\end_document
"""


templates['llncs'] = r"""
\lyxformat 508
\begin_document
\begin_header
\save_transient_properties true
\origin unavailable
\textclass llncs
\begin_preamble
${preamble}
\end_preamble
\use_default_options true
\maintain_unincluded_children false
\language english
\language_package default
\inputencoding auto
\fontencoding global
\font_roman "default" "default"
\font_sans "default" "default"
\font_typewriter "default" "default"
\font_math "auto" "auto"
\font_default_family default
\use_non_tex_fonts false
\font_sc false
\font_osf false
\font_sf_scale 100 100
\font_tt_scale 100 100
\graphics default
\default_output_format default
\output_sync 0
\bibtex_command default
\index_command default
\paperfontsize default
\spacing single
\use_hyperref false
\papersize default
\use_geometry false
\use_package amsmath 1
\use_package amssymb 1
\use_package cancel 1
\use_package esint 1
\use_package mathdots 1
\use_package mathtools 1
\use_package mhchem 1
\use_package stackrel 1
\use_package stmaryrd 1
\use_package undertilde 1
\cite_engine basic
\cite_engine_type default
\biblio_style plain
\use_bibtopic false
\use_indices false
\paperorientation portrait
\suppress_date false
\justification true
\use_refstyle 0
\index Index
\shortcut idx
\color #008000
\end_index
\secnumdepth 3
\tocdepth 3
\paragraph_separation indent
\paragraph_indentation default
\quotes_language english
\papercolumns 1
\papersides 1
\paperpagestyle default
\tracking_changes false
\output_changes false
\html_math_output 0
\html_css_as_file 0
\html_be_strict false
\end_header

\begin_body

${content}

\end_body
\end_document
"""
