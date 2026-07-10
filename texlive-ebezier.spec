%global tl_name ebezier
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4
Release:	%{tl_revision}.1
Summary:	Device independent picture environment enhancement
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ebezier
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ebezier.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ebezier.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ebezier.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Ebezier is a device independent extension for the standard picture
environment. Linear, quadratic, and cubic bezier curves are supplied in
connection with higher level circle drawing commands. Additionally some
macros for the calculation of curve lengths are part of this package.

