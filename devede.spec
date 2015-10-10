%define oname devedeng

Name:		devede
Version:	4.2
Release:	1
Summary:	Graphical frontend to create video DVDs/(S)VCDs
License:	GPLv3+
Group:		Graphical desktop/Other
URL:		http://www.rastersoft.com/programas/devede.html
Source0:	http://www.rastersoft.com/descargas/%{oname}-%{version}.tar.bz2
# Created from upstream .svg icon by GIMP - ImageMagick does not do well
# at converting .svg on the fly - AdamW 2007/09
Source1:	devede-16.png
Source2:	devede-32.png
Source3:	devede-48.png
BuildArch:	noarch
BuildRequires:	bash
BuildRequires:	coreutils
Requires:	dvdauthor
Requires:	mencoder
Requires:	mkisofs
Requires:	mplayer
Requires:	pygtk2.0
Requires:	python3
Requires:	vcdimager
Requires:	python3-cairo

%description
DeVeDe is a program to create video DVDs (compatible with home players) from
nearly any video format. It only uses Python, MPlayer, Mencoder, DVDAuthor,
VCDImager, and mkisofs, so it has very few dependencies.

%prep
%setup -q -n %{oname}

# remove shebangs...
%__sed -i -e '/^#!\//, 1d' %{oname}_*.py

%build
%__sed -i 's/\/usr\/lib\/devede/\/usr\/share\/devede/' %{oname}

%install
# The stuff that goes to /usr/lib is just python scripts, not actually
# arch-specific. The app always looks for them in /usr/lib , even on
# x86-64. So define libdir as %_prefix/lib. See bug #31692. -AdamW 2007/06
DESTDIR=%{buildroot} \
prefix=%{_prefix} \
libdir=%{_datadir}/ \
	./install.sh

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
%{_bindir}/%{oname}
%{_bindir}/%{oname}_debug
%defattr(0644,root,root,0755)
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/%{oname}
%{_datadir}/doc/%{oname}
%{_iconsdir}/hicolor/*/apps/%{oname}.*

