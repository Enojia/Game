" All system-wide defaults are set in $VIMRUNTIME/archlinux.vim (usually just
" /usr/share/vim/vimfiles/archlinux.vim) and sourced by the call to :runtime
" you can find below.  If you wish to change any of those settings, you should
" do it in this file (/etc/vimrc), since archlinux.vim will be overwritten
" everytime an upgrade of the vim packages is performed.  It is recommended to
" make changes after sourcing archlinux.vim since it alters the value of the
" 'compatible' option.

" This line should not be removed as it ensures that various options are
" properly set to work with the Vim-related packages.
runtime! archlinux.vim

" If you prefer the old-style vim functionalty, add 'runtime! vimrc_example.vim'
" Or better yet, read /usr/share/vim/vim74/vimrc_example.vim or the vim manual
" and configure vim to your own liking!

set nocompatible
filetype off
filetype plugin on

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'

Plugin 'tmhedberg/SimpylFold'

Plugin 'vim-scripts/indentpython.vim'

Plugin 'vim-scripts/Pydiction'

Plugin 'Valloric/YouCompleteMe'

Plugin 'scrooloose/syntastic'

Plugin 'nvie/vim-flake8'

call vundle#end()
filetype plugin indent on


" Enable folding

set foldmethod=indent
set foldlevel=99

" Enable folding with the spacebar
nnoremap <space> za

au BufNewFile,BufRead *.py
	\set tabstop=4
	\set softtabstop=4
	\set shiftwidth=4
	\set textwidth=79
	\set expandtab
	\set autoindent
	\set fileformat=unix

set encoding=utf-8

let g:ycm_autoclose_preview_window_after_completion=1
map <leader>g :YcmCompleter GoToDefinitionElseDeclaration<CR>

"python with virtualenv support
py << EOF
import os
import sys
if 'VIRTUA_ENV' in os.environ:
	project_base_dir = os.environ['VIRTUAL_ENV']
	sys.path.insert(0, project_base_dir)
	activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
	execfile(activate_this, dict(__file__=activate_this))
EOF

let python_hightlight_all=1
syntax on
let g:pydiction_location = '/home/enojia/.vim/bundle/Pydiction/complete-dict'
set nu
