%define oname devedeng

Summary:		Graphical frontend to create video DVDs/(S)VCDs
Name:		devede
Version:		4.21.3.1
Release:		2
License:		GPLv3+
Group:	Graphics
Url:		https://www.rastersoft.com/programas/devede.html
Source0:	https://gitlab.com/rastersoft/devedeng/-/archive/%{version}/%{oname}-%{version}.tar.bz2
# Created from upstream .svg icon by GIMP - ImageMagick does not do well
# at converting .svg on the fly - AdamW 2007/09
Source1:	devede-16.png
Source2:	devede-32.png
Source3:	devede-48.png
Patch0:	devede-4.21.0-fix-env-shebangs.patch
BuildRequires:		bash
BuildRequires:		coreutils
BuildRequires:		locales-extra-charsets
BuildRequires:		pkgconfig(python3)
BuildRequires:		python%{pyver}dist(hatchling)
BuildRequires:		python%{pyver}dist(pip)
BuildRequires:		python%{pyver}dist(pyproject-api)
BuildRequires:		python%{pyver}dist(setuptools)
BuildRequires:		python%{pyver}dist(wheel)
BuildArch:		noarch
Requires:	dvdauthor
Requires:	ffmpeg
Requires:	mkisofs
Requires:	python >= 3.12
Requires:	python-cairo
Requires:	python%{pyver}dist(setuptools)
Requires:	typelib(Gtk) = 3.0
Requires:	vcdimager
Recommends:	k3b
Recommends:	mpv
Recommends:	vlc


%description
DeVeDe NG is a program to create video DVDs (compatible with home players)
from nearly any video format. It only uses Python, Mpv, Mencoder, DVDAuthor,
VCDImager and mkisofs, so it has very few dependencies.

%files
#-f %%{oname}.lang
%doc src/%{oname}/data/doc/*
%{_bindir}/%{name}_ng
%{_datadir}/applications/%{name}_ng.desktop
#{_datadir}/%%{oname}
#{_datadir}/doc/%%{oname}
%{_datadir}/metainfo/com.rastersoft.%{oname}.appdata.xml
%{_iconsdir}/hicolor/*/apps/%{oname}.*
%{_iconsdir}/hicolor/scalable/apps/%{oname}_icon.svg
%{_mandir}/man1/%{name}.1*
%{py_puresitedir}/%{oname}
%{py_puresitedir}/%{oname}-4.21.3.dist-info
%{py_puresitedir}/copy_files_verbose.py
%{py_puresitedir}/__pycache__/copy_files_verbose.cpython-3*.pyc

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-%{version}


%build
%py_build


%install
%py_install

# Icons
mkdir -p %{buildroot}/%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
install -m 644 %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{oname}.png
install -m 644 %{SOURCE2} %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{oname}.png
install -m 644 %{SOURCE3} %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{oname}.png

# Install other useful stuff not installed by default
mkdir -p %{buildroot}/%{_mandir}/man1
mkdir -p %{buildroot}/%{_datadir}/metainfo/
install -m 0644 src/%{oname}/data/%{name}.1 %{buildroot}/%{_mandir}/man1
install -m 0644 src/%{oname}/data/com.rastersoft.%{oname}.appdata.xml %{buildroot}/%{_datadir}/metainfo/

# Fix perms
chmod +x %{buildroot}%{py_puresitedir}/copy_files_verbose.py
chmod +x %{buildroot}%{py_puresitedir}/%{oname}/{__init__,avbase,avconv,avprobe,configuration_data,devedeng,dvdauthor_converter,executor,ffmpeg}.py
chmod +x %{buildroot}%{py_puresitedir}/%{oname}/{ffprobe,file_copy,genisoimage,help,mkisofs,mplayer,mpv,mux_dvd_menu,subtitles_mux,vcdimager_converter}.py

#find_lang %%{oname}
