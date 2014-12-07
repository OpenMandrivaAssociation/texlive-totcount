# revision 21178
# category Package
# catalog-ctan /macros/latex/contrib/totcount
# catalog-date 2011-01-25 21:21:41 +0100
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-totcount
Version:	1.2
Release:	9
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 757037
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 719782
- texlive-totcount
- texlive-totcount
- texlive-totcount

