#
# Conditional build:
%bcond_without	cppcheck	# cppcheck to check geany-plugins source code

Summary:	A collection of different plugins for Geany
Summary(pl.UTF-8):	Zbiór różnych wtyczek dla Geany
Name:		geany-plugins
Version:	2.0
Release:	3
License:	GPL v2+
Group:		Libraries
Source0:	https://plugins.geany.org/geany-plugins/%{name}-%{version}.tar.gz
# Source0-md5:	87b17a7f3ea2402f2bbd5ca68771aafb
Patch0:		gcc14.patch
URL:		https://plugins.geany.org/
BuildRequires:	autoconf >= 2.61
BuildRequires:	autoconf-archive
BuildRequires:	automake >= 1:1.8
BuildRequires:	check-devel
%{?with_cppcheck:BuildRequires:	cppcheck}
BuildRequires:	ctpl-devel >= 0.3
BuildRequires:	docutils
BuildRequires:	enchant2-devel >= 2.2
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	geany-devel >= 2.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.22
BuildRequires:	gpgme-devel >= 0.4.2
BuildRequires:	gtk+3-devel >= 3.24
#BuildRequires:	gtk-webkit3-devel >= 1.1.18
BuildRequires:	gtk-webkit4-devel >= 1.1.18
BuildRequires:	gtkspell3-devel >= 3.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libgit2-devel >= 0.21
BuildRequires:	libmarkdown-devel
BuildRequires:	libsoup-devel >= 2.42
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	lua51-devel >= 5.1
BuildRequires:	pkgconfig
BuildRequires:	vala
BuildRequires:	vte-devel >= 0.46
Requires:	geany >= 2.0
Requires:	glib2 >= 1:2.22
Obsoletes:	geany-plugins-devhelp < 1.37
Obsoletes:	geany-plugins-geanypy < 1.37
Obsoletes:	geany-plugins-multiterm < 1.37
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Geany-Plugins is a collection of different plugins for Geany, a
lightweight IDE.

%description -l pl.UTF-8
Geany-Plugins to zbiór różnych wtyczek dla Geany, lekiego IDE
używającego GTK+.

%package addons
Summary:	Various small plugins for Geany
Summary(pl.UTF-8):	Różne drobne dodatki dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description addons
This plugin adds various small addons to Geany which aren't worth an
own plugin but might still useful for people.

%description addons -l pl.UTF-8
Ta wtyczka dodaje różne małe dodatki do Geany, które nie zasługują aby
mieć własne wtyczki, ale wciąż są użyteczne dla ludzi.

%package autoclose
Summary:	autoclose plugin for Geany
Summary(pl.UTF-8):	Wtyczka automatycznego zamykania nawiasów dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description autoclose
This plugin enables auto-closing features.

%description autoclose -l pl.UTF-8
Ta wtyczka automatycznie zamyka nawiasy w trakcie pisania kodu.

%package automark
Summary:	automark plugin for Geany
Summary(pl.UTF-8):	Wtyczka automark dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description automark
This is a simple plugin that highlights all words that match current
word under cursor.

%description automark -l pl.UTF-8
Ta wtyczka podświetla wszystkie słowa pasujące do aktualnie
znajdującego się pod kursorem.

%package codenav
Summary:	codenav plugin for Geany
Summary(pl.UTF-8):	Wtyczka codenav dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description codenav
This plugin adds some facilities for navigating in code files.

%description codenav -l pl.UTF-8
Wtyczka ułatwiająca nawigowanie po kodzie.

%package commander
Summary:	commander plugin for Geany
Summary(pl.UTF-8):	Wtyczka commander dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description commander
Commander is a plugin for Geany that provides a command panel for
rapid access to any action.

%description commander -l pl.UTF-8
Commander to wtyczka do Geany, która zapewnia panel poleceń,
umożliwiający szybki dostęp do dowolnej akcji.

%package debugger
Summary:	debugger plugin for Geany
Summary(pl.UTF-8):	Wtyczka debugger dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description debugger
Plugin enables debugging in Geany. Currently supports GDB only, but
was developed with multiple debuggers support in mind, so the other
backends support is planned as well.

%description debugger -l pl.UTF-8
Wtyczka umożliwia debugowanie w Geany. Obecnie obsługuje tylko GDB,
ale została opracowana z myślą o obsłudze wielu debuggerów, więc
planowane jest także wsparcie innych backendów.

%package defineformat
Summary:	defineformat plugin for Geany
Summary(pl.UTF-8):	Wtyczka defineformat dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description defineformat
Defineformat -- on-the-fly #define prettyprinter. This plugin will
help you to write multiline defines with aligned backslash.

%description defineformat -l pl.UTF-8
Ta wtyczka pomaga pisać definicje wielowierszowe z wyrównanym
odwrotnym ukośnikiem.

%package geanyctags
Summary:	geanyctags plugin for Geany
Summary(pl.UTF-8):	Wtyczka geanyctags dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ctags

%description geanyctags
GeanyCtags adds a simple support for generating and querying ctags
files for a Geany project. It requires that the ctags command is
installed in a system path

%description geanyctags -l pl.UTF-8
GeanyCtags dodaje prostą obsługę generowania i sprawdzania plików
ctags dla projektu Geany. Wtyczka wymaga zainstalowanego ctags.

%package geanydoc
Summary:	geanydoc plugin for Geany
Summary(pl.UTF-8):	Wtyczka geanydoc dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description geanydoc
Geanydoc is plugin for Geany IDE that allow execute specified commands
on the current word at the cursor position.

%description geanydoc -l pl.UTF-8
Geanydoc to wtyczka dla IDE Geany, która pozwala wykonywać określone
polecenia dla aktualnie zaznaczonego słowa.

%package geanyextrasel
Summary:	geanyextrasel plugin for Geany
Summary(pl.UTF-8):	Wtyczka geanyextrasel dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description geanyextrasel
The Extra Selection plugin adds the following functions to Geany:
- Goto matching brace and select (Select to Matching Brace).
- Goto line and select (Select to Line).
- Toggle the current selection type between stream and rectangular
  (without changing column mode, can be invoked while drag-selecting).
- Ctrl-Shift-Alt-Left/Right/Home/End keys - same as Ctrl-Shift, but
  for rectangular selection.
- Column mode - while active, all (Ctrl)-Shift-movement keys do
  rectangle selection instead of stream.
- Selection with anchor instead of the Shift-movement keys.

%description geanyextrasel -l pl.UTF-8
Wtyczka Extra Selection dodaje do Geany następujące funkcje:
- Przejście do pasującego nawiasu klamrowego i zaznaczenie (Zaznacz do
  pasującego nawiasu klamrowego),
- Przejście do linii i zaznaczenie (Zaznacz do linii).
- Przełączanie bieżącego rodzaju zaznaczenia między strumieniowym a
  prostokątnym (bez zmiany trybu kolumnowego, można wywoływać podczas
  zaznaczania przeciągnięciem).
- Ctrl-Shift-Alt-Left / Right / Home / End - tak samo jak Ctrl-Shift,
  ale dla zaznaczania prostokątnego.
- Tryb kolumnowy - gdy aktywny, wszystkie klawisze (Ctrl)-Shift-ruch
  wykonują zaznaczenie prostokątne zamiast strumieniowego.
- Zaznaczanie za pomocą kotwicy zamiast klawiszy Shift-move.

%package geanygendoc
Summary:	geanygendoc plugin for Geany
Summary(pl.UTF-8):	Wtyczka geanygendoc dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ctpl >= 0.3
# rst2html
Requires:	docutils

%description geanygendoc
GeanyGenDoc is a plugin for Geany that aims to help code documentation
by automatically generating documentation comment basis from the
source code.

%description geanygendoc -l pl.UTF-8
GeanyGenDoc to wtyczka Geany wspomagająca dokumentowanie kodu poprzez
automatyczne generowanie podstaw komentarzy dokumenujących z kodu
źródłowego.

%package geanyinsertnum
Summary:	geanyinsertnum plugin for Geany
Summary(pl.UTF-8):	Wtyczka geanyinsertnum dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description geanyinsertnum
This plugin replaces a (possibly zero-width) rectangular selection
with integer numbers, using start/step/base etc. specified by the
user. For practical reasons, the number of lines is limited to 250000.
Lines shorter than the current selection are skipped.

%description geanyinsertnum -l pl.UTF-8
Wtyczka ta zastępuje prostokątne zaznaczenie (także o zerowej
szerokości) ciągiem liczb całkowitych, określony przez początek, krok,
podstawę itp. podane przez użytkownika. Ze względów praktycznych
liczba linii jest ograniczona do 250000. Linie krótsze niż bieżące
zaznaczenie są pomijane.

%package geanylua
Summary:	geanylua plugin for Geany
Summary(pl.UTF-8):	Wtyczka geanylua dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description geanylua
This is a plugin for the Geany IDE to provide Lua scripting.

%description geanylua -l pl.UTF-8
Ta wtyczka umożliwia używanie w Geany skryptów LUA.

%package geanymacro
Summary:	geanymacro plugin for Geany
Summary(pl.UTF-8):	Wtyczka geanymacro dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description geanymacro
Geanymacro is a plugin to provide user defined macros for Geany

%description geanymacro -l pl.UTF-8
Geanymacro to wtyczka pozwalająca użytkownikowi definiować własne
makra.

%package geanyminiscript
Summary:	geanyminiscript plugin for Geany
Summary(pl.UTF-8):	Wtyczka geanyminiscript dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description geanyminiscript
A Geany Mini-Script filter plugin

%description geanyminiscript -l pl.UTF-8
Wtyczka filtra Geany Mini-Script

%package geanynumberedbookmarks
Summary:	geanynumberedbookmarks plugin for Geany
Summary(pl.UTF-8):	Wtyczka geanynumberedbookmarks dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description geanynumberedbookmarks
Geanynumberedbookmarks is a plugin to provide users with 10 numbered
bookmarks (in addition to the usual bookmarks).

%description geanynumberedbookmarks -l pl.UTF-8
Geanynumberedbookmarks to wtyczka zapewniająca użytkownikom 10
ponumerowanych zakładek (oprócz zwykłych zakładek).

%package geanypg
Summary:	geanypg plugin for Geany
Summary(pl.UTF-8):	Wtyczka geanypg dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description geanypg
GeanyPG is a plugin for Geany that allows the user to encrypt, decrypt
and verify signatures with GnuPG.

%description geanypg -l pl.UTF-8
GeanyPG to wtyczka dla Geany, która pozwala użytkownikowi szyfrować,
odszyfrowywać i weryfikować podpisy za pomocą GnuPG.

%package geanyprj
Summary:	geanyprj plugin for Geany
Summary(pl.UTF-8):	Wtyczka geanyprj dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description geanyprj
Geanyprj is alternative project manager for Geany fast light IDE.

%description geanyprj -l pl.UTF-8
Geanyprj jest alternatywnym zarządcą projektów dla Geany IDE.

%package geanyvc
Summary:	geanyvc plugin for Geany
Summary(pl.UTF-8):	Wtyczka geanyvc dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description geanyvc
GeanyVC is plugin that provides a uniform way of accessing the
different version-control systems inside Geany IDE. Only small subset
of vc is implemented, but, hey, you don't need anything besides diff,
log, status, revert and commit most time.

%description geanyvc -l pl.UTF-8
GeanyVC to wtyczka, która zapewnia jednolity sposób dostępu do różnych
systemów kontroli wersji w IDE Geany. Zaimplementowano tylko niewielki
podzbiór funkcji, ale zwykle wystarczają różnice, log zmian, status,
wycofywanie i zatwierdzanie zmian.

%package geniuspaste
Summary:	geniuspaste plugin for Geany
Summary(pl.UTF-8):	Wtyczka geniuspaste dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description geniuspaste
This plugin allows the user to paste code from Geany into a configured
pastebin service. At the moment it ships with builtin support these
pastebin services, but more can be added:
- codepad.org
- dpaste.de
- fpaste.org
- pastebin.geany.org
- paste.debian.net
- sprunge.us

GeniusPaste detects automatically the syntax of the code and pastes it
with syntax highlighting enabled. It can also display the pasted code
opening a new browser tab.

%description geniuspaste -l pl.UTF-8
Ta wtyczka pozwala użytkownikowi wkleić kod z Geany do skonfigurowanej
usługi pastebin. W tej chwili ma wbudowaną obsługę poniższych usłg
pastebin, ale może być dodane więcej:
- codepad.org
- dpaste.de
- fpaste.org
- pastebin.geany.org
- paste.debian.net
- sprunge.us

GeniusPaste automatycznie wykrywa składnię kodu i wkleja go z
włączonym podświetlaniem składni. Może także wyświetlać wklejony kod,
otwierając nową kartę przeglądarki.

%package git-changebar
Summary:	git-changebar plugin for Geany
Summary(pl.UTF-8):	Wtyczka git-changebar dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description git-changebar
This plugin highlights uncommitted changes to files tracked with Git,
allows to navigate through the hunks and undo them.

%description git-changebar -l pl.UTF-8
Ta wtyczka podkreśla niezatwierdzone zmiany w plikach śledzonych za
pomocą Gita, pozwala nawigować między zmienionymi blokami i wycofywać
zmiany.

%package keyrecord
Summary:	keyrecord plugin for Geany
Summary(pl.UTF-8):	Wtyczka keyrecord dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description keyrecord
This plugin allows you to record a sequence of keystrokes and to
replay it several times.

%description keyrecord -l pl.UTF-8
Ta wtyczka pozwala nagrywać sekwencję naciśnięć klawiszy i odtwarzać
ją kilka razy.

%package latex
Summary:	latex plugin for Geany
Summary(pl.UTF-8):	Wtyczka latex dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description latex
LaTeX is a little plugin to improve support of LaTeX on Geany.

%description latex -l pl.UTF-8
LaTeX to prosta wtyczka rozszerzająca możliwości Geany w tym zakresie.

%package lineoperations
Summary:	lineoperations plugin for Geany
Summary(pl.UTF-8):	Wtyczka lineoperations dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description lineoperations
Line Operations is an assortment of simple line functions that can be
applied to an open file, or selection.

%description lineoperations -l pl.UTF-8
Line Operations to zestaw prostych, operujących na liniach funkcji,
które można zastosować do otwartego pliku lub zaznaczenia.

%package lipsum
Summary:	lipsum plugin for Geany
Summary(pl.UTF-8):	Wtyczka lipsum dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description lipsum
Lipsum is a plugin for Geany that implements a Lorem Ipsum generator
to insert placeholder text into your document.

%description lipsum -l pl.UTF-8
Lipsum to wtyczka dla Geany, która implementuje generator Lorem Ipsum
do wstawiania tekstu zastępczego do dokumentu.

%package markdown
Summary:	markdown plugin for Geany
Summary(pl.UTF-8):	Wtyczka markdown dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description markdown
This plugin provides a real-time preview of rendered Markdown, that
is, Markdown converted to HTML and inserted into an HTML template and
loaded into a WebKit view.

%description markdown -l pl.UTF-8
Ta wtyczka zapewnia podgląd w czasie rzeczywistym renderowanego kodu
Markdown, tzn. Markdown jest konwertowany na HTML i wstawiany do
szablonu HTML, a następnie ładowany do widoku WebKit.

%package overview
Summary:	overview plugin for Geany
Summary(pl.UTF-8):	Wtyczka overview dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description overview
The Overview plugin is a small zoomed-out view next to the normal
editor view that allows to see and navigate a lot of the file at once.
It is similar to the Minimap in SublimeText or such similar feature in
numerous other editors.

%description overview -l pl.UTF-8
Wtyczka Overview to mały, pomniejszony widok obok normalnego widoku
edytora, który pozwala zobaczyć i nawigować po wielu plikach
jednocześnie. Jest podobny do Minimapy w SublimeText lub podobnej
funkcji w wielu innych edytorach.

%package pairtaghighlighter
Summary:	pairtaghighlighter plugin for Geany
Summary(pl.UTF-8):	Wtyczka pairtaghighlighter dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description pairtaghighlighter
Finds and highlights matching opening/closing HTML tag by clicking or
moving cursor inside a tag.

%description pairtaghighlighter -l pl.UTF-8
Ta wtyczka znajduje i wyróżnia pasujący otwierający/zamykający
znacznik HTML po kliknięciu albo przesunięciu kursora wewnątrz
znacznika.

%package pohelper
Summary:	pohelper plugin for Geany
Summary(pl.UTF-8):	Wtyczka pohelper dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description pohelper
Translation Helper is a plugin for Geany that improves the support for
GetText translation files, by providing various features specific to
this format and to translators.

%description pohelper -l pl.UTF-8
Translation Helper to wtyczka dla Geany, która usprawnia obsługę
plików tłumaczeń GetTexta, zapewniając różne funkcje specyficzne dla
tego formatu i dla tłumaczy.

%package pretty-printer
Summary:	pretty-printer plugin for Geany
Summary(pl.UTF-8):	Wtyczka pretty-printer dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxml2 >= 1:2.6.27

%description pretty-printer
Formats an XML file and makes it human-readable.

%description pretty-printer -l pl.UTF-8
Formatuje XML i czyni go czytelnym dla ludzi.

%package projectorganizer
Summary:	projectorganizer plugin for Geany
Summary(pl.UTF-8):	Wtyczka projectorganizer dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description projectorganizer
Project Organizer is an extension of Geany's project management
displaying a tree of files belonging to the project in the sidebar.

%description projectorganizer -l pl.UTF-8
Project Organizer to rozszerzenie zarządzania projektami Geany,
wyświetlające na pasku bocznym drzewo plików należących do projektu.

%package scope
Summary:	scope plugin for Geany
Summary(pl.UTF-8):	Wtyczka scope dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description scope
Scope is a graphical GDB front-end with the normal functions you would
expect (stepping, breakpoints...), and a few notable features:
- The comminication between Scope and gdb is asynchronous.
- You can enter any gdb command, at any time (of course, for the
  command to be executed, gdb must be[come] available).
- All gdb I/O (along with some other messages) is displayed in a
  terminal-like "Debug Console". Whenever you find the GUI lacking,
  simply switch to that console and work directly with gdb.
- 7-bit/Locale/UTF-8 support for values.

%description scope -l pl.UTF-8
Scope jest graficznym interfejsem do GDB ze zwykłymi funkcjami,
których można oczekiwać (krokami, punktami przerwania itp.) i kilkoma
ważnymi cechami:
- Łączność między Scope a gdb jest asynchroniczna.
- Można wprowadzić dowolne polecenie gdb w dowolnym momencie
  (oczywiście, aby polecenie zostało wykonane, gdb musi być dostępne).
- Wszystkie wejścia/wyjścia gdb (wraz z kilkoma innymi komunikatami)
  są wyświetlane w podobnej do terminalu „konsoli debugowania”.
  Jeżeli czegokolwiek brakuje w GUI, wystarczy przełączyć na tę
  konsolę i pracować bezpośrednio z gdb.
- Obsługa znaków 7-bitowych/zlokalizowanych/UTF-8.

%package sendmail
Summary:	sendmail plugin for Geany
Summary(pl.UTF-8):	Wtyczka sendmail dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description sendmail
SendMail is a little plugin to send a document as attachment using the
preferred mail client from inside Geany. It is similar to the envelope
symbol of most office tools and requires a mail client that is
supporting remote calls. This is not a direct binding to sendmail,
even if it could be used for.

%description sendmail -l pl.UTF-8
SendMail to mała wtyczka do wysyłania dokumentu jako załącznika przy
użyciu preferowanego klienta poczty z Geany. Jest podobna do symbolu
koperty większości narzędzi biurowych i wymaga klienta poczty
obsługującego połączenia zdalne. Nie jest bezpośrednio powiązana z
sendmailem, nawet jeśli to sendmail miałby być używany do poczty.

%package shiftcolumn
Summary:	shiftcolumn plugin for Geany
Summary(pl.UTF-8):	Wtyczka shiftcolumn dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description shiftcolumn
This plugin allows you to move blocks of text horizontally in left or
right direction skipping one character at a time.

%description shiftcolumn -l pl.UTF-8
Ta wtyczka umożliwia przenoszenie bloków tekstu poziomo w lewo lub w
prawo, przeskakując jeden znak na raz.

%package spellcheck
Summary:	spellcheck plugin for Geany
Summary(pl.UTF-8):	Wtyczka spellcheck dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	enchant2 >= 2.2

%description spellcheck
This plugin checks the content of the current document in Geany with
the spell check library Enchant. You can also select a certain text
passage, then the plugin will only check the selected text. All lines
with misspelled words are highlighted with a red squiggly underline
and the wrong words are printed in the messages window at the bottom
of Geany together with available suggestions. For the plugin to work
at all, you need to have the Enchant library installed together with
at least one backend (Aspell, Myspell, Hunspell, ...). The plugin's
configure dialog lists all available languages/dictionaries which can
be used for the spell check.

%description spellcheck -l pl.UTF-8
Ta wtyczka sprawdza pisownię bieżącego dokumentu w Geany za pomocą
biblioteki sprawdzania pisowni Enchant. Można także wybrać określony
fragment tekstu, a wtyczka sprawdzi tylko zaznaczony tekst. Wszystkie
wiersze z błędnie napisanymi słowami są podświetlone czerwonym
zawijasowym podkreśleniem, a nieprawidłowe słowa są wypisywane w oknie
wiadomości u dołu Geany wraz z dostępnymi podpowiedziami. Aby wtyczka
w ogóle działała, trzeba mieć zainstalowaną bibliotekę Enchant z co
najmniej jednym backendem (Aspell, Myspell, Hunspell...). Okno
dialogowe konfiguracji wtyczki zawiera listę wszystkich dostępnych
języków/słowników, których można użyć do sprawdzania pisowni.

%package tableconvert
Summary:	tableconvert plugin for Geany
Summary(pl.UTF-8):	Wtyczka tableconvert dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description tableconvert
Tableconvert is a plugin which helps on converting a tabulator
separated selection into a table.

%description tableconvert -l pl.UTF-8
Tableconvert to wtyczka, która pomaga w konwertowaniu zaznaczenia
porozdzielanego tabulatorami na tabelę.

%package treebrowser
Summary:	treebrowser plugin for Geany
Summary(pl.UTF-8):	Wtyczka treebrowser dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description treebrowser
The TreeBrowser plugin for Geany provides an alternate way to browse
through your files. It displays files and directories in a tree view
and has more features than the file browser plugin delivered with
Geany itself.

%description treebrowser -l pl.UTF-8
Wtyczka TreeBrowser dla Geany zapewnia alternatywny sposób
przeglądania plików. Wyświetla pliki i katalogi w widoku drzewa i ma
więcej funkcji niż wtyczka przeglądarki plików dostarczana z samym
Geany.

%package updatechecker
Summary:	updatechecker plugin for Geany
Summary(pl.UTF-8):	Wtyczka updatechecker dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libsoup >= 2.42

%description updatechecker
UpdateChecker is a plugin for Geany, which is able to check whether
there is a more recent version of Geany available.

%description updatechecker -l pl.UTF-8
UpdateChecker to wtyczka dla Geany, która może sprawdzić, czy dostępna
jest nowsza wersja Geany.

%package vimode
Summary:	vimode plugin for Geany
Summary(pl.UTF-8):	Wtyczka vimode dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description vimode
Vimode is a Vim-mode plugin for Geany.

%description vimode -l pl.UTF-8
Vimode to wtyczka trybu Vim dla Geany.

%package webhelper
Summary:	webhelper plugin for Geany
Summary(pl.UTF-8):	: Wtyczka webhelper dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description webhelper
WebHelper is a plugin for Geany that provides some web development
facilities, such as a web page preview and some debugging tools (web
inspector).

%description webhelper -l pl.UTF-8
WebHelper to wtyczka dla Geany, która zapewnia pewne funkcje
programistyczne, takie jak podgląd strony internetowej i niektóre
narzędzia diagnostyczne (web inspector).

%package workbench
Summary:	workbench plugin for Geany
Summary(pl.UTF-8):	Wtyczka workbench dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description workbench
The Workbench plugin is an extension that makes it possible to manage
multiple projects in geany. You can add geany projects to a workbench.
From there you can add directories to the project to manage the files
belonging to the project.

%description workbench -l pl.UTF-8
Wtyczka Workbench jest rozszerzeniem, które umożliwia zarządzanie
wieloma projektami w Geany. Pozwala dodawać projekty Geany do "biurka
roboczego". Stamtąd można dodawać do projektu katalogi, aby zarządzać
plikami należącymi do projektu.

%package xmlsnippets
Summary:	xmlsnippets plugin for Geany
Summary(pl.UTF-8):	Wtyczka xmlsnippets dla Geany
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description xmlsnippets
This plugin extends XML/HTML tag autocompletion provided by Geany. It
automatically inserts a matching snippet after you type an opening
tag.

%description xmlsnippets -l pl.UTF-8
Ta wtyczka rozszerza automatyczne uzupełnianie znaczników XML/HTML
dostarczane przez Geany. Automatycznie wstawia pasujący fragment po
wpisaniu otwierającego znacznika.

%prep
%setup -q
%patch -P 0 -p1
%{__rm} build/bundled/gpgme.m4

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I build
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	%{!?with_cppcheck:--disable-cppcheck} \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/{,geany/,%{name}/geanylua/}*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgeanypluginutils.so

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libgeanypluginutils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgeanypluginutils.so.0
%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}

%files addons
%defattr(644,root,root,755)
%doc addons/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/addons.so

%files autoclose
%defattr(644,root,root,755)
%doc autoclose/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/autoclose.so

%files automark
%defattr(644,root,root,755)
%doc automark/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/automark.so

%files codenav
%defattr(644,root,root,755)
%doc codenav/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/codenav.so

%files commander
%defattr(644,root,root,755)
%doc commander/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/commander.so

%files debugger
%defattr(644,root,root,755)
%doc commander/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/debugger.so
%{_datadir}/%{name}/debugger

%files defineformat
%defattr(644,root,root,755)
%doc defineformat/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/defineformat.so

%files geanyctags
%defattr(644,root,root,755)
%doc geanyctags/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/geanyctags.so

%files geanydoc
%defattr(644,root,root,755)
%doc geanydoc/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/geanydoc.so

%files geanyextrasel
%defattr(644,root,root,755)
%doc geanyextrasel/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/geanyextrasel.so

%files geanygendoc
%defattr(644,root,root,755)
%doc geanygendoc/{AUTHORS,ChangeLog,NEWS,README,TODO}
%attr(755,root,root) %{_libdir}/geany/geanygendoc.so
%{_datadir}/%{name}/geanygendoc

%files geanyinsertnum
%defattr(644,root,root,755)
%doc geanyinsertnum/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/geanyinsertnum.so

%files geanylua
%defattr(644,root,root,755)
%doc geanylua/{AUTHORS,ChangeLog,NEWS,README} geanylua/docs/*.html
%attr(755,root,root) %{_libdir}/geany/geanylua.so
%dir %{_libdir}/%{name}/geanylua
%attr(755,root,root) %{_libdir}/%{name}/geanylua/*.so
%{_datadir}/%{name}/geanylua

%files geanymacro
%defattr(644,root,root,755)
%doc geanymacro/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/geanymacro.so

%files geanyminiscript
%defattr(644,root,root,755)
%doc geanyminiscript/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/geanyminiscript.so

%files geanynumberedbookmarks
%defattr(644,root,root,755)
%doc geanynumberedbookmarks/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/geanynumberedbookmarks.so

%files geanypg
%defattr(644,root,root,755)
%doc geanypg/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/geanypg.so

%files geanyprj
%defattr(644,root,root,755)
%doc geanyprj/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/geanyprj.so

%files geanyvc
%defattr(644,root,root,755)
%doc geanyvc/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/geanyvc.so

%files geniuspaste
%defattr(644,root,root,755)
%doc geniuspaste/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/geniuspaste.so
%{_datadir}/%{name}/geniuspaste

%files git-changebar
%defattr(644,root,root,755)
%doc git-changebar/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/git-changebar.so
%{_datadir}/%{name}/git-changebar

%files keyrecord
%defattr(644,root,root,755)
%doc keyrecord/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/keyrecord.so

%files latex
%defattr(644,root,root,755)
%doc latex/{AUTHORS,ChangeLog,NEWS,README} latex/doc/latex.pdf
%attr(755,root,root) %{_libdir}/geany/latex.so

%files lineoperations
%defattr(644,root,root,755)
%doc lineoperations/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/lineoperations.so

%files lipsum
%defattr(644,root,root,755)
%doc lipsum/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/lipsum.so

%files markdown
%defattr(644,root,root,755)
%doc markdown/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/markdown.so

%files overview
%defattr(644,root,root,755)
%doc overview/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/overview.so
%{_datadir}/%{name}/overview

%files pairtaghighlighter
%defattr(644,root,root,755)
%doc pairtaghighlighter/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/pairtaghighlighter.so

%files pohelper
%defattr(644,root,root,755)
%doc pohelper/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/pohelper.so
%{_datadir}/%{name}/pohelper

%files pretty-printer
%defattr(644,root,root,755)
%doc pretty-printer/{AUTHORS,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/pretty-printer.so

%files projectorganizer
%defattr(644,root,root,755)
%doc projectorganizer/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/projectorganizer.so

%files scope
%defattr(644,root,root,755)
%doc scope/{AUTHORS,ChangeLog,NEWS,README} scope/docs/*.html
%attr(755,root,root) %{_libdir}/geany/scope.so
%{_datadir}/%{name}/scope

%files sendmail
%defattr(644,root,root,755)
%doc sendmail/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/sendmail.so

%files shiftcolumn
%defattr(644,root,root,755)
%doc shiftcolumn/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/shiftcolumn.so

%files spellcheck
%defattr(644,root,root,755)
%doc spellcheck/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/spellcheck.so

%files tableconvert
%defattr(644,root,root,755)
%doc tableconvert/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/tableconvert.so

%files treebrowser
%defattr(644,root,root,755)
%doc treebrowser/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/treebrowser.so

%files updatechecker
%defattr(644,root,root,755)
%doc updatechecker/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/updatechecker.so

%files vimode
%defattr(644,root,root,755)
%doc vimode/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/vimode.so

%files webhelper
%defattr(644,root,root,755)
%doc webhelper/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/webhelper.so

%files workbench
%defattr(644,root,root,755)
%doc workbench/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/workbench.so

%files xmlsnippets
%defattr(644,root,root,755)
%doc xmlsnippets/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/geany/xmlsnippets.so
