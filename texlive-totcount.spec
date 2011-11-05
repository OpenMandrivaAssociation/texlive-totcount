# revision 21178
# category Package
# catalog-ctan /macros/latex/contrib/totcount
# catalog-date 2011-01-25 21:21:41 +0100
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-totcount
Version:	1.2
Release:	1
Summary:	Find the last value of a counter
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/totcount
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/totcount.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/totcount.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/totcount.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package records the value that was last set, for any
counter of interest; since most such counters are simply
incremented when they are changed, the recorded value will
usually be the maximum value.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
