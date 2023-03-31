Name:		texlive-totcount
Version:	21178
Release:	2
Summary:	Find the last value of a counter
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/totcount
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/totcount.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/totcount.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/totcount.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package records the value that was last set, for any
counter of interest; since most such counters are simply
incremented when they are changed, the recorded value will
usually be the maximum value.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/totcount/totcount.sty
%doc %{_texmfdistdir}/doc/latex/totcount/README
%doc %{_texmfdistdir}/doc/latex/totcount/totcount-ex.tex
%doc %{_texmfdistdir}/doc/latex/totcount/totcount.pdf
#- source
%doc %{_texmfdistdir}/source/latex/totcount/totcount.drv
%doc %{_texmfdistdir}/source/latex/totcount/totcount.dtx
%doc %{_texmfdistdir}/source/latex/totcount/totcount.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
