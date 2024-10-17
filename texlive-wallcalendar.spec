Name:		texlive-wallcalendar
Version:	45568
Release:	2
Summary:	A wall calendar class with custom layouts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/wallcalendar
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wallcalendar.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wallcalendar.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a wall calendar class with custom layouts
and support for internationalization. It comes with the
following layouts: Full page photo, the calendar days overlaid
with opacity Full page photo, the photo above the calendar days
Small landscape photo, with a calendar grid Year planner
Thumbnails and captions Varnish mask There is also support for
loading event marks from a CSV file.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/wallcalendar
%doc %{_texmfdistdir}/doc/lualatex/wallcalendar

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
