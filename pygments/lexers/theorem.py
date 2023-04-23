"""
    pygments.lexers.theorem
    ~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for theorem-proving languages.

    :copyright: Copyright 2006-2022 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer, default, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Generic, Whitespace

__all__ = ['CoqLexer', 'IsabelleLexer', 'LeanLexer', 'SquirrelLexer']

class SquirrelLexer(RegexLexer):
    """
    For the Squirrel protocol prover.

    .. versionadded:: 1.0
    """

    name = 'Squirrel'
    url = 'https://squirrel-prover.github.io/'
    aliases = ['squirrel']
    filenames = ['*.sp']
    mimetypes = ['text/x-squirrel']

    flags = 0 # no re.MULTILINE

    keywords_prog = (
        "let",
        "in",
        "out",
        "if",
        "then",
        "else",
        "fun",
        "new",
        "try find",
        "such that",
    )

    keywords_glob = (
        "include",
        "set",
        "axiom",
        "goal",
        "global",
        "local",
        "Proof",
        "Qed",
        "equiv",
        "any",
    )

    keywords_dangerous = (
        "Abort",
        "admit",
        "Reset",
    )

    keywords_decl = (
        "aenc",
        "signature",
        "hash",
        "senc",
        "abstract",
        "op",
        "system",
        "type",
        "name",
        "action",
        "channel",
        "mutable",
        "process",
        "with oracle",
        "with hash",
        "where",
    )

    keywords_fun = (
        "input",
        "cond",
        "output",
        "exec",
        "frame",
        "seq",
        "diff",
        "happens",
        "len",
        "xor",
    )

    keywords_type = (
        "index",
        "message",
        "boolean",
        "bool",
        "timestamp",
        "large",
        "name_fixed_length",
    )

    keywords_tactic = (
        "anyintro",
        "use",
        "with",
        "assert",
        "trans",
        "sym",
        "have",
        "case",
        "const",
        "collision",
        "depends",
        "eqnames",
        "eqtraces",
        "euf",
        "executable",
        "exists",
        "Exists",
        "splitseq",
        "remember",
        "expand",
        "fresh",
        "forall",
        "Forall",
        "help",
        "id",
        "cs",
        "clear",
        "prof",
        "induction",
        "intro",
        "apply",
        "generalize",
        "dependent",
        "revert",
        "destruct",
        "as",
        "left",
        "notleft",
        "print",
        "search",
        "project",
        "right",
        "simpl",
        "reduce",
        "simpl_left",
        "split",
        "subst",
        "rewrite",
        "true",
        "cca1",
        "ddh",
        "gdh",
        "cdh",
        "enckp",
        "enrich",
        "equivalent",
        "expandall",
        "fa",
        "show",
        "deduce",
        "fresh",
        "prf",
        "trivialif",
        "xor",
        "intctxt",
        "splitseq",
        "constseq",
        "localize",
        "memseq",
        "byequiv",
        "diffeq",
        "gcca",
        "rename",
        "gprf",
    )

    keywords_closing = (
        "by",
        "assumption",
        "congruence",
        "constraints",
        "auto",
        "refl",
        "hint",
    )

    keywords_tactical = (
        "try",
        "orelse",
        "repeat",
        "nosimpl",
        "checkfail",
        "exn",
    )

    # Mostly taken from Coq lexer but not (yet) all in squirrel language
    keyopts = (
        '!=', '#', '&', '&&', r'\(', r'\)', r'\*', r'\+', ',', '-', r'-\.',
        '->', r'\.', r'\.\.', ':', '::', ':=', ':>', ';', ';;', '<', '<-',
        '<->', '=', '>', '>]', r'>\}', r'\?', r'\?\?', r'\[', r'\[<', r'\[>',
        r'\[\|', ']', '_', '`', r'\{', r'\{<', r'\|', r'\|]', r'\}', '~', '=>',
        r'/\\', r'\\/', r'\{\|', r'\|\}',
        # 'Π', 'Σ', # Not defined in the standard library
        'λ', '¬', '∧', '∨', '∀', '∃', '→', '↔', '≠', '≤', '≥',
    )
    operators = r'[!$%&*+\./:<=>?@^|~-]'
    prefix_syms = r'[!?~]'
    infix_syms = r'[=<>@^|&+\*/$%-]'

    # Mostly taken from Coq lexer but not (yet) all in squirrel language
    tokens = {
        'root': [
            (r'\s+', Text),
            (r'false|true|\(\)|\[\]', Name.Builtin.Pseudo),
            (r'\(\*', Comment, 'comment'),
            (r'\b(?:[^\W\d][\w\']*\.)+[^\W\d][\w\']*\b', Name),
            (words(keywords_glob, prefix=r'\b', suffix=r'\b'), Keyword.Namespace),
            (words(keywords_prog, prefix=r'\b', suffix=r'\b'), Keyword),
            (words(keywords_type, prefix=r'\b', suffix=r'\b'), Keyword.Type),
            (r'\b\'[a-z]*[a-z_\'1-9]*\b', Keyword.Type),
            (words(keywords_dangerous, prefix=r'\b', suffix=r'\b'),Generic.Error),
            (words(keywords_decl, prefix=r'\b', suffix=r'\b'),Keyword.Declaration),
            (words(keywords_tactic, prefix=r'\b', suffix=r'\b'), Keyword),
            (words(keywords_closing, prefix=r'\b', suffix=r'\b'), Keyword.Pseudo),
            (words(keywords_tactical, prefix=r'\b', suffix=r'\b'), Keyword.Reserved),
            (words(keywords_fun, prefix=r'\b', suffix=r'\b'), Name.Function),

            (r'\b([A-Z][\w\']*)', Name),
            (r'(%s)' % '|'.join(keyopts[::-1]), Operator),
            (r'(%s|%s)?%s' % (infix_syms, prefix_syms, operators), Operator),

            (r"[^\W\d][\w']*", Name),

            # Not in Squirrel but still better to have ↓
            (r'\d[\d_]*', Number.Integer),
            (r'0[xX][\da-fA-F][\da-fA-F_]*', Number.Hex),
            (r'0[oO][0-7][0-7_]*', Number.Oct),
            (r'0[bB][01][01_]*', Number.Bin),
            (r'-?\d[\d_]*(.[\d_]*)?([eE][+\-]?\d[\d_]*)', Number.Float),

            (r"'(?:(\\[\\\"'ntbr ])|(\\[0-9]{3})|(\\x[0-9a-fA-F]{2}))'", String.Char),

            (r"'.'", String.Char),
            (r"'", Keyword),  # a stray quote is another syntax element

            (r'[~?][a-z][\w\']*:', Name),
            (r'\S', Name.Builtin.Pseudo),
        ],
        'comment': [
            (r'[^(*)]+', Comment),
            (r'\(\*', Comment, '#push'),
            (r'\*\)', Comment, '#pop'),
            (r'[(*)]', Comment),
        ],
        # We may have different highlight rules when in a Proof…
    }

    def analyse_text(text):
        if 'Qed' in text and 'Proof' in text:
            return 1

class CoqLexer(RegexLexer):
    """
    For the Coq theorem prover.

    .. versionadded:: 1.5
    """

    name = 'Coq'
    url = 'http://coq.inria.fr/'
    aliases = ['coq']
    filenames = ['*.v']
    mimetypes = ['text/x-coq']

    flags = 0 # no re.MULTILINE

    keywords1 = (
        # Vernacular commands
        'Section', 'Module', 'End', 'Require', 'Import', 'Export', 'Variable',
        'Variables', 'Parameter', 'Parameters', 'Axiom', 'Axioms', 'Hypothesis',
        'Hypotheses', 'Notation', 'Local', 'Tactic', 'Reserved', 'Scope',
        'Open', 'Close', 'Bind', 'Delimit', 'Definition', 'Example', 'Let',
        'Ltac', 'Fixpoint', 'CoFixpoint', 'Morphism', 'Relation', 'Implicit',
        'Arguments', 'Types', 'Unset', 'Contextual', 'Strict', 'Prenex',
        'Implicits', 'Inductive', 'CoInductive', 'Record', 'Structure',
        'Variant', 'Canonical', 'Coercion', 'Theorem', 'Lemma', 'Fact',
        'Remark', 'Corollary', 'Proposition', 'Property', 'Goal',
        'Proof', 'Restart', 'Save', 'Qed', 'Defined', 'Abort', 'Admitted',
        'Hint', 'Resolve', 'Rewrite', 'View', 'Search', 'Compute', 'Eval',
        'Show', 'Print', 'Printing', 'All', 'Graph', 'Projections', 'inside',
        'outside', 'Check', 'Global', 'Instance', 'Class', 'Existing',
        'Universe', 'Polymorphic', 'Monomorphic', 'Context', 'Scheme', 'From',
        'Undo', 'Fail', 'Function',
    )
    keywords2 = (
        # Gallina
        'forall', 'exists', 'exists2', 'fun', 'fix', 'cofix', 'struct',
        'match', 'end',  'in', 'return', 'let', 'if', 'is', 'then', 'else',
        'for', 'of', 'nosimpl', 'with', 'as',
    )
    keywords3 = (
        # Sorts
        'Type', 'Prop', 'SProp', 'Set',
    )
    keywords4 = (
        # Tactics
        'pose', 'set', 'move', 'case', 'elim', 'apply', 'clear', 'hnf', 'intro',
        'intros', 'generalize', 'rename', 'pattern', 'after', 'destruct',
        'induction', 'using', 'refine', 'inversion', 'injection', 'rewrite',
        'congr', 'unlock', 'compute', 'ring', 'field', 'replace', 'fold',
        'unfold', 'change', 'cutrewrite', 'simpl', 'have', 'suff', 'wlog',
        'suffices', 'without', 'loss', 'nat_norm', 'assert', 'cut', 'trivial',
        'revert', 'bool_congr', 'nat_congr', 'symmetry', 'transitivity', 'auto',
        'split', 'left', 'right', 'autorewrite', 'tauto', 'setoid_rewrite',
        'intuition', 'eauto', 'eapply', 'econstructor', 'etransitivity',
        'constructor', 'erewrite', 'red', 'cbv', 'lazy', 'vm_compute',
        'native_compute', 'subst',
    )
    keywords5 = (
        # Terminators
        'by', 'now', 'done', 'exact', 'reflexivity',
        'tauto', 'romega', 'omega', 'lia', 'nia', 'lra', 'nra', 'psatz',
        'assumption', 'solve', 'contradiction', 'discriminate',
        'congruence', 'admit'
    )
    keywords6 = (
        # Control
        'do', 'last', 'first', 'try', 'idtac', 'repeat',
    )
    # 'as', 'assert', 'begin', 'class', 'constraint', 'do', 'done',
    # 'downto', 'else', 'end', 'exception', 'external', 'false',
    # 'for', 'fun', 'function', 'functor', 'if', 'in', 'include',
    # 'inherit', 'initializer', 'lazy', 'let', 'match', 'method',
    # 'module', 'mutable', 'new', 'object', 'of', 'open', 'private',
    # 'raise', 'rec', 'sig', 'struct', 'then', 'to', 'true', 'try',
    # 'type', 'val', 'virtual', 'when', 'while', 'with'
    keyopts = (
        '!=', '#', '&', '&&', r'\(', r'\)', r'\*', r'\+', ',', '-', r'-\.',
        '->', r'\.', r'\.\.', ':', '::', ':=', ':>', ';', ';;', '<', '<-',
        '<->', '=', '>', '>]', r'>\}', r'\?', r'\?\?', r'\[', r'\[<', r'\[>',
        r'\[\|', ']', '_', '`', r'\{', r'\{<', r'\|', r'\|]', r'\}', '~', '=>',
        r'/\\', r'\\/', r'\{\|', r'\|\}',
        # 'Π', 'Σ', # Not defined in the standard library
        'λ', '¬', '∧', '∨', '∀', '∃', '→', '↔', '≠', '≤', '≥',
    )
    operators = r'[!$%&*+\./:<=>?@^|~-]'
    prefix_syms = r'[!?~]'
    infix_syms = r'[=<>@^|&+\*/$%-]'

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'false|true|\(\)|\[\]', Name.Builtin.Pseudo),
            (r'\(\*', Comment, 'comment'),
            (r'\b(?:[^\W\d][\w\']*\.)+[^\W\d][\w\']*\b', Name),
            (r'\bEquations\b\??', Keyword.Namespace),
            # Very weak heuristic to distinguish the Set vernacular from the Set sort
            (r'\bSet(?=[ \t]+[A-Z][a-z][^\n]*?\.)', Keyword.Namespace),
            (words(keywords1, prefix=r'\b', suffix=r'\b'), Keyword.Namespace),
            (words(keywords2, prefix=r'\b', suffix=r'\b'), Keyword),
            (words(keywords3, prefix=r'\b', suffix=r'\b'), Keyword.Type),
            (words(keywords4, prefix=r'\b', suffix=r'\b'), Keyword),
            (words(keywords5, prefix=r'\b', suffix=r'\b'), Keyword.Pseudo),
            (words(keywords6, prefix=r'\b', suffix=r'\b'), Keyword.Reserved),
            # (r'\b([A-Z][\w\']*)(\.)', Name.Namespace, 'dotted'),
            (r'\b([A-Z][\w\']*)', Name),
            (r'(%s)' % '|'.join(keyopts[::-1]), Operator),
            (r'(%s|%s)?%s' % (infix_syms, prefix_syms, operators), Operator),

            (r"[^\W\d][\w']*", Name),

            (r'\d[\d_]*', Number.Integer),
            (r'0[xX][\da-fA-F][\da-fA-F_]*', Number.Hex),
            (r'0[oO][0-7][0-7_]*', Number.Oct),
            (r'0[bB][01][01_]*', Number.Bin),
            (r'-?\d[\d_]*(.[\d_]*)?([eE][+\-]?\d[\d_]*)', Number.Float),

            (r"'(?:(\\[\\\"'ntbr ])|(\\[0-9]{3})|(\\x[0-9a-fA-F]{2}))'", String.Char),

            (r"'.'", String.Char),
            (r"'", Keyword),  # a stray quote is another syntax element

            (r'"', String.Double, 'string'),

            (r'[~?][a-z][\w\']*:', Name),
            (r'\S', Name.Builtin.Pseudo),
        ],
        'comment': [
            (r'[^(*)]+', Comment),
            (r'\(\*', Comment, '#push'),
            (r'\*\)', Comment, '#pop'),
            (r'[(*)]', Comment),
        ],
        'string': [
            (r'[^"]+', String.Double),
            (r'""', String.Double),
            (r'"', String.Double, '#pop'),
        ],
        'dotted': [
            (r'\s+', Text),
            (r'\.', Punctuation),
            (r'[A-Z][\w\']*(?=\s*\.)', Name.Namespace),
            (r'[A-Z][\w\']*', Name.Class, '#pop'),
            (r'[a-z][a-z0-9_\']*', Name, '#pop'),
            default('#pop')
        ],
    }

    def analyse_text(text):
        if 'Qed' in text and 'Proof' in text:
            return 1


class IsabelleLexer(RegexLexer):
    """
    For the Isabelle proof assistant.

    .. versionadded:: 2.0
    """

    name = 'Isabelle'
    url = 'https://isabelle.in.tum.de/'
    aliases = ['isabelle']
    filenames = ['*.thy']
    mimetypes = ['text/x-isabelle']

    keyword_minor = (
        'and', 'assumes', 'attach', 'avoids', 'binder', 'checking',
        'class_instance', 'class_relation', 'code_module', 'congs',
        'constant', 'constrains', 'datatypes', 'defines', 'file', 'fixes',
        'for', 'functions', 'hints', 'identifier', 'if', 'imports', 'in',
        'includes', 'infix', 'infixl', 'infixr', 'is', 'keywords', 'lazy',
        'module_name', 'monos', 'morphisms', 'no_discs_sels', 'notes',
        'obtains', 'open', 'output', 'overloaded', 'parametric', 'permissive',
        'pervasive', 'rep_compat', 'shows', 'structure', 'type_class',
        'type_constructor', 'unchecked', 'unsafe', 'where',
    )

    keyword_diag = (
        'ML_command', 'ML_val', 'class_deps', 'code_deps', 'code_thms',
        'display_drafts', 'find_consts', 'find_theorems', 'find_unused_assms',
        'full_prf', 'help', 'locale_deps', 'nitpick', 'pr', 'prf',
        'print_abbrevs', 'print_antiquotations', 'print_attributes',
        'print_binds', 'print_bnfs', 'print_bundles',
        'print_case_translations', 'print_cases', 'print_claset',
        'print_classes', 'print_codeproc', 'print_codesetup',
        'print_coercions', 'print_commands', 'print_context',
        'print_defn_rules', 'print_dependencies', 'print_facts',
        'print_induct_rules', 'print_inductives', 'print_interps',
        'print_locale', 'print_locales', 'print_methods', 'print_options',
        'print_orders', 'print_quot_maps', 'print_quotconsts',
        'print_quotients', 'print_quotientsQ3', 'print_quotmapsQ3',
        'print_rules', 'print_simpset', 'print_state', 'print_statement',
        'print_syntax', 'print_theorems', 'print_theory', 'print_trans_rules',
        'prop', 'pwd', 'quickcheck', 'refute', 'sledgehammer', 'smt_status',
        'solve_direct', 'spark_status', 'term', 'thm', 'thm_deps', 'thy_deps',
        'try', 'try0', 'typ', 'unused_thms', 'value', 'values', 'welcome',
        'print_ML_antiquotations', 'print_term_bindings', 'values_prolog',
    )

    keyword_thy = ('theory', 'begin', 'end')

    keyword_section = ('header', 'chapter')

    keyword_subsection = (
        'section', 'subsection', 'subsubsection', 'sect', 'subsect',
        'subsubsect',
    )

    keyword_theory_decl = (
        'ML', 'ML_file', 'abbreviation', 'adhoc_overloading', 'arities',
        'atom_decl', 'attribute_setup', 'axiomatization', 'bundle',
        'case_of_simps', 'class', 'classes', 'classrel', 'codatatype',
        'code_abort', 'code_class', 'code_const', 'code_datatype',
        'code_identifier', 'code_include', 'code_instance', 'code_modulename',
        'code_monad', 'code_printing', 'code_reflect', 'code_reserved',
        'code_type', 'coinductive', 'coinductive_set', 'consts', 'context',
        'datatype', 'datatype_new', 'datatype_new_compat', 'declaration',
        'declare', 'default_sort', 'defer_recdef', 'definition', 'defs',
        'domain', 'domain_isomorphism', 'domaindef', 'equivariance',
        'export_code', 'extract', 'extract_type', 'fixrec', 'fun',
        'fun_cases', 'hide_class', 'hide_const', 'hide_fact', 'hide_type',
        'import_const_map', 'import_file', 'import_tptp', 'import_type_map',
        'inductive', 'inductive_set', 'instantiation', 'judgment', 'lemmas',
        'lifting_forget', 'lifting_update', 'local_setup', 'locale',
        'method_setup', 'nitpick_params', 'no_adhoc_overloading',
        'no_notation', 'no_syntax', 'no_translations', 'no_type_notation',
        'nominal_datatype', 'nonterminal', 'notation', 'notepad', 'oracle',
        'overloading', 'parse_ast_translation', 'parse_translation',
        'partial_function', 'primcorec', 'primrec', 'primrec_new',
        'print_ast_translation', 'print_translation', 'quickcheck_generator',
        'quickcheck_params', 'realizability', 'realizers', 'recdef', 'record',
        'refute_params', 'setup', 'setup_lifting', 'simproc_setup',
        'simps_of_case', 'sledgehammer_params', 'spark_end', 'spark_open',
        'spark_open_siv', 'spark_open_vcg', 'spark_proof_functions',
        'spark_types', 'statespace', 'syntax', 'syntax_declaration', 'text',
        'text_raw', 'theorems', 'translations', 'type_notation',
        'type_synonym', 'typed_print_translation', 'typedecl', 'hoarestate',
        'install_C_file', 'install_C_types', 'wpc_setup', 'c_defs', 'c_types',
        'memsafe', 'SML_export', 'SML_file', 'SML_import', 'approximate',
        'bnf_axiomatization', 'cartouche', 'datatype_compat',
        'free_constructors', 'functor', 'nominal_function',
        'nominal_termination', 'permanent_interpretation',
        'binds', 'defining', 'smt2_status', 'term_cartouche',
        'boogie_file', 'text_cartouche',
    )

    keyword_theory_script = ('inductive_cases', 'inductive_simps')

    keyword_theory_goal = (
        'ax_specification', 'bnf', 'code_pred', 'corollary', 'cpodef',
        'crunch', 'crunch_ignore',
        'enriched_type', 'function', 'instance', 'interpretation', 'lemma',
        'lift_definition', 'nominal_inductive', 'nominal_inductive2',
        'nominal_primrec', 'pcpodef', 'primcorecursive',
        'quotient_definition', 'quotient_type', 'recdef_tc', 'rep_datatype',
        'schematic_corollary', 'schematic_lemma', 'schematic_theorem',
        'spark_vc', 'specification', 'subclass', 'sublocale', 'termination',
        'theorem', 'typedef', 'wrap_free_constructors',
    )

    keyword_qed = ('by', 'done', 'qed')
    keyword_abandon_proof = ('sorry', 'oops')

    keyword_proof_goal = ('have', 'hence', 'interpret')

    keyword_proof_block = ('next', 'proof')

    keyword_proof_chain = (
        'finally', 'from', 'then', 'ultimately', 'with',
    )

    keyword_proof_decl = (
        'ML_prf', 'also', 'include', 'including', 'let', 'moreover', 'note',
        'txt', 'txt_raw', 'unfolding', 'using', 'write',
    )

    keyword_proof_asm = ('assume', 'case', 'def', 'fix', 'presume')

    keyword_proof_asm_goal = ('guess', 'obtain', 'show', 'thus')

    keyword_proof_script = (
        'apply', 'apply_end', 'apply_trace', 'back', 'defer', 'prefer',
    )

    operators = (
        '::', ':', '(', ')', '[', ']', '_', '=', ',', '|',
        '+', '-', '!', '?',
    )

    proof_operators = ('{', '}', '.', '..')

    tokens = {
        'root': [
            (r'\s+', Whitespace),
            (r'\(\*', Comment, 'comment'),
            (r'\\<open>', String.Symbol, 'cartouche'),
            (r'\{\*|‹', String, 'cartouche'),

            (words(operators), Operator),
            (words(proof_operators), Operator.Word),

            (words(keyword_minor, prefix=r'\b', suffix=r'\b'), Keyword.Pseudo),

            (words(keyword_diag, prefix=r'\b', suffix=r'\b'), Keyword.Type),

            (words(keyword_thy, prefix=r'\b', suffix=r'\b'), Keyword),
            (words(keyword_theory_decl, prefix=r'\b', suffix=r'\b'), Keyword),

            (words(keyword_section, prefix=r'\b', suffix=r'\b'), Generic.Heading),
            (words(keyword_subsection, prefix=r'\b', suffix=r'\b'), Generic.Subheading),

            (words(keyword_theory_goal, prefix=r'\b', suffix=r'\b'), Keyword.Namespace),
            (words(keyword_theory_script, prefix=r'\b', suffix=r'\b'), Keyword.Namespace),

            (words(keyword_abandon_proof, prefix=r'\b', suffix=r'\b'), Generic.Error),

            (words(keyword_qed, prefix=r'\b', suffix=r'\b'), Keyword),
            (words(keyword_proof_goal, prefix=r'\b', suffix=r'\b'), Keyword),
            (words(keyword_proof_block, prefix=r'\b', suffix=r'\b'), Keyword),
            (words(keyword_proof_decl, prefix=r'\b', suffix=r'\b'), Keyword),

            (words(keyword_proof_chain, prefix=r'\b', suffix=r'\b'), Keyword),
            (words(keyword_proof_asm, prefix=r'\b', suffix=r'\b'), Keyword),
            (words(keyword_proof_asm_goal, prefix=r'\b', suffix=r'\b'), Keyword),

            (words(keyword_proof_script, prefix=r'\b', suffix=r'\b'), Keyword.Pseudo),

            (r'\\<(\w|\^)*>', Text.Symbol),

            (r"'[^\W\d][.\w']*", Name.Type),

            (r'0[xX][\da-fA-F][\da-fA-F_]*', Number.Hex),
            (r'0[oO][0-7][0-7_]*', Number.Oct),
            (r'0[bB][01][01_]*', Number.Bin),

            (r'"', String, 'string'),
            (r'`', String.Other, 'fact'),
            (r'[^\s:|\[\]\-()=,+!?{}._][^\s:|\[\]\-()=,+!?{}]*', Name),
        ],
        'comment': [
            (r'[^(*)]+', Comment),
            (r'\(\*', Comment, '#push'),
            (r'\*\)', Comment, '#pop'),
            (r'[(*)]', Comment),
        ],
        'cartouche': [
            (r'[^{*}\\‹›]+', String),
            (r'\\<open>', String.Symbol, '#push'),
            (r'\{\*|‹', String, '#push'),
            (r'\\<close>', String.Symbol, '#pop'),
            (r'\*\}|›', String, '#pop'),
            (r'\\<(\w|\^)*>', String.Symbol),
            (r'[{*}\\]', String),
        ],
        'string': [
            (r'[^"\\]+', String),
            (r'\\<(\w|\^)*>', String.Symbol),
            (r'\\"', String),
            (r'\\', String),
            (r'"', String, '#pop'),
        ],
        'fact': [
            (r'[^`\\]+', String.Other),
            (r'\\<(\w|\^)*>', String.Symbol),
            (r'\\`', String.Other),
            (r'\\', String.Other),
            (r'`', String.Other, '#pop'),
        ],
    }


class LeanLexer(RegexLexer):
    """
    For the Lean theorem prover.

    .. versionadded:: 2.0
    """
    name = 'Lean'
    url = 'https://github.com/leanprover/lean'
    aliases = ['lean']
    filenames = ['*.lean']
    mimetypes = ['text/x-lean']

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'/--', String.Doc, 'docstring'),
            (r'/-', Comment, 'comment'),
            (r'--.*?$', Comment.Single),
            (words((
                'import', 'renaming', 'hiding',
                'namespace',
                'local',
                'private', 'protected', 'section',
                'include', 'omit', 'section',
                'protected', 'export',
                'open',
                'attribute',
            ), prefix=r'\b', suffix=r'\b'), Keyword.Namespace),
            (words((
                'lemma', 'theorem', 'def', 'definition', 'example',
                'axiom', 'axioms', 'constant', 'constants',
                'universe', 'universes',
                'inductive', 'coinductive', 'structure', 'extends',
                'class', 'instance',
                'abbreviation',

                'noncomputable theory',

                'noncomputable', 'mutual', 'meta',

                'attribute',

                'parameter', 'parameters',
                'variable', 'variables',

                'reserve', 'precedence',
                'postfix', 'prefix', 'notation', 'infix', 'infixl', 'infixr',

                'begin', 'by', 'end',

                'set_option',
                'run_cmd',
            ), prefix=r'\b', suffix=r'\b'), Keyword.Declaration),
            (r'@\[[^\]]*\]', Keyword.Declaration),
            (words((
                'forall', 'fun', 'Pi', 'from', 'have', 'show', 'assume', 'suffices',
                'let', 'if', 'else', 'then', 'in', 'with', 'calc', 'match',
                'do'
            ), prefix=r'\b', suffix=r'\b'), Keyword),
            (words(('sorry', 'admit'), prefix=r'\b', suffix=r'\b'), Generic.Error),
            (words(('Sort', 'Prop', 'Type'), prefix=r'\b', suffix=r'\b'), Keyword.Type),
            (words((
                '#eval', '#check', '#reduce', '#exit',
                '#print', '#help',
            ), suffix=r'\b'), Keyword),
            (words((
                '(', ')', ':', '{', '}', '[', ']', '⟨', '⟩', '‹', '›', '⦃', '⦄', ':=', ',',
            )), Operator),
            (r'[A-Za-z_\u03b1-\u03ba\u03bc-\u03fb\u1f00-\u1ffe\u2100-\u214f]'
             r'[.A-Za-z_\'\u03b1-\u03ba\u03bc-\u03fb\u1f00-\u1ffe\u2070-\u2079'
             r'\u207f-\u2089\u2090-\u209c\u2100-\u214f0-9]*', Name),
            (r'0x[A-Za-z0-9]+', Number.Integer),
            (r'0b[01]+', Number.Integer),
            (r'\d+', Number.Integer),
            (r'"', String.Double, 'string'),
            (r"'(?:(\\[\\\"'nt])|(\\x[0-9a-fA-F]{2})|(\\u[0-9a-fA-F]{4})|.)'", String.Char),
            (r'[~?][a-z][\w\']*:', Name.Variable),
            (r'\S', Name.Builtin.Pseudo),
        ],
        'comment': [
            (r'[^/-]', Comment.Multiline),
            (r'/-', Comment.Multiline, '#push'),
            (r'-/', Comment.Multiline, '#pop'),
            (r'[/-]', Comment.Multiline)
        ],
        'docstring': [
            (r'[^/-]', String.Doc),
            (r'-/', String.Doc, '#pop'),
            (r'[/-]', String.Doc)
        ],
        'string': [
            (r'[^\\"]+', String.Double),
            (r"(?:(\\[\\\"'nt])|(\\x[0-9a-fA-F]{2})|(\\u[0-9a-fA-F]{4}))", String.Escape),
            ('"', String.Double, '#pop'),
        ],
    }
