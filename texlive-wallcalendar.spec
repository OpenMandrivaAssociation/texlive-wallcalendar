%global tl_name wallcalendar
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6.0
Release:	%{tl_revision}.1
Summary:	A wall calendar class with custom layouts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/wallcalendar
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wallcalendar.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wallcalendar.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a wall calendar class with custom layouts and
support for internationalization. It comes with the following layouts:
Full page photo, the calendar days overlaid with opacity Full page
photo, the photo above the calendar days Small landscape photo, with a
calendar grid Year planner Thumbnails and captions Varnish mask There is
also support for loading event marks from a CSV file.

