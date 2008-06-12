Name:       	devede
Version:    	3.6
Release:    	%mkrel 1
Summary:    	Graphical frontend to create video DVDs
License:    	GPLv3+
Group:      	Graphical desktop/Other
URL:        	http://www.rastersoft.com/programas/devede.html
Source0:     	http://www.rastersoft.com/descargas/%{name}-%{version}.tar.bz2
# Created from upstream .svg icon by GIMP - ImageMagick does not do well
# at converting .svg on the fly - AdamW 2007/09
Source1:	devede-16.png
Source2:	devede-32.png
Source3:	devede-48.png
BuildRoot:  	%_tmppath/%name-buildroot
BuildArch:	noarch
BuildRequires:	bash
BuildRequires:	coreutils
Requires:   	dvdauthor
Requires:   	mencoder
Requires:   	mkisofs
Requires:   	mplayer
Requires:   	pygtk2.0
Requires:   	pygtk2.0-libglade
Requires:   	python
%ifarch %ix86
Requires:   	python-psyco
%endif
Requires:   	vcdimager
Requires:	python-cairo
Requires(post,postun): desktop-common-data

%description
DeVeDe is a program to create video DVDs (compatible with home players) from
nearly any video format. It only uses Python, MPlayer, Mencoder, DVDAuthor,
VCDImager, and mkisofs, so it has very few dependencies.

%prep
%setup -q

%build

%install
# The stuff that goes to /usr/lib is just python scripts, not actually
# arch-specific. The app always looks for them in /usr/lib , even on
# x86-64. So define libdir as %_prefix/lib. See bug #31692. -AdamW 2007/06
rm -rf %buildroot
DESTDIR=%buildroot \
prefix=%_prefix \
libdir=%_prefix/lib \
	./install.sh

# fd.o icons
mkdir -p %buildroot%_iconsdir/hicolor/{16x16,32x32,48x48,scalable}/apps
mv %buildroot%_datadir/pixmaps/%{name}.svg %buildroot%_iconsdir/hicolor/scalable/apps/%{name}.svg
install -m 644 %{SOURCE1} %buildroot%_iconsdir/hicolor/16x16/apps/%{name}.png
install -m 644 %{SOURCE2} %buildroot%_iconsdir/hicolor/32x32/apps/%{name}.png
install -m 644 %{SOURCE3} %buildroot%_iconsdir/hicolor/48x48/apps/%{name}.png

%find_lang %name

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(0755,root,root,0755)
%_bindir/%{name}
%defattr(0644,root,root,0755)
%_datadir/applications/%{name}.desktop
%_datadir/%{name}
%_datadir/doc/%{name}
%_iconsdir/hicolor/*/apps/%{name}.*
%_prefix/lib/%{name}
