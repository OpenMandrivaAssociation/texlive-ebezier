# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/ebezier
# catalog-date 2009-01-30 10:13:19 +0100
# catalog-license lppl
# catalog-version 4
Name:		texlive-ebezier
Version:	4
Release:	1
Summary:	Device independent picture environment enhancement
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ebezier
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebezier.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebezier.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebezier.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Ebezier is a device independent extension for the standard
picture environment. Linear, quadratic, and cubic bezier curves
are supplied in connection with higher level circle drawing
commands. Additionally some macros for the calculation of curve
lenghts are part of this package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ebezier/ebezier.sty
%doc %{_texmfdistdir}/doc/latex/ebezier/ebezier.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ebezier/ebezier.dtx
%doc %{_texmfdistdir}/source/latex/ebezier/ebezier.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
