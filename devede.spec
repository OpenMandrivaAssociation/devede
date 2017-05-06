%define oname devedeng

Name:		devede
Version:	4.8.8
Release:	2
Summary:	Graphical frontend to create video DVDs/(S)VCDs
License:	GPLv3+
Group:		Graphical desktop/Other
URL:		http://www.rastersoft.com/programas/devede.html
Source0:	http://www.rastersoft.com/descargas/%{oname}-%{version}.tar.gz
# Created from upstream .svg icon by GIMP - ImageMagick does not do well
# at converting .svg on the fly - AdamW 2007/09
Source1:	devede-16.png
Source2:	devede-32.png
Source3:	devede-48.png
BuildArch:	noarch
BuildRequires:	bash
BuildRequires:	coreutils
BuildRequires:	python-setuptools
Requires:	dvdauthor
Requires:	mencoder
Requires:	mkisofs
Requires:	mplayer
Requires:	typelib(Gtk) = 3.0
Requires:	python
Requires:	vcdimager
Requires:	python-cairo
Requires:	python-pkg-resources

%description
DeVeDe is a program to create video DVDs (compatible with home players) from
nearly any video format. It only uses Python, MPlayer, Mencoder, DVDAuthor,
VCDImager, and mkisofs, so it has very few dependencies.

%prep
%setup -q -n %{oname}-%{version}

%build
python setup.py build

%install

python setup.py install --root=%{buildroot}

# fd.o icons
mkdir -p %{buildroot}/%{_iconsdir}/hicolor/{16x16,32x32,48x48,scalable}/apps
mv %{buildroot}/%{_datadir}/pixmaps/%{oname}.svg %{buildroot}/%{_iconsdir}/hicolor/scalable/apps/%{oname}.svg
install -m 644 %{SOURCE1} %{buildroot}/%{_iconsdir}/hicolor/16x16/apps/%{oname}.png
install -m 644 %{SOURCE2} %{buildroot}/%{_iconsdir}/hicolor/32x32/apps/%{oname}.png
install -m 644 %{SOURCE3} %{buildroot}/%{_iconsdir}/hicolor/48x48/apps/%{oname}.png

# redundant files, temp files...
rm -f %{buildroot}/%{_bindir}/%{oname}-debug
rm -f %{buildroot}/%{_datadir}/doc/%{oname}/html/*~

%find_lang %{oname}

%files -f %{oname}.lang
%defattr(0755,root,root,0755)
%{_bindir}/devede_ng.py
%{_bindir}/copy_files_verbose.py
%defattr(0644,root,root,0755)
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/%{oname}
%{_datadir}/doc/%{oname}
%{py_puresitedir}/%{oname}*
%{_iconsdir}/hicolor/*/apps/%{oname}.*
%{_mandir}/man1/%{name}*
