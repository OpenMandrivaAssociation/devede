Name:       	devede
Version:    	3.0
Release:    	%mkrel 2
Summary:    	Graphical frontend to create video DVDs
License:    	GPL
Group:      	Graphical desktop/Other
URL:        	http://www.rastersoft.com/programas/devede.html
Source:     	http://www.rastersoft.com/descargas/%{name}-%{version}.tar.bz2
BuildRoot:  	%_tmppath/%name-buildroot
BuildRequires:	bash
BuildRequires:	coreutils
BuildRequires:	imagemagick
Requires:   	dvdauthor
Requires:   	mencoder
Requires:   	mkisofs
Requires:   	mplayer
Requires:   	pygtk2.0
Requires:   	python
%ifarch %ix86
Requires:   	python-psyco
%endif
Requires:   	vcdimager
Requires(post,postun): desktop-common-data

%description
DeVeDe is a program to create video DVDs (compatible with home players) from
nearly any video format. It only uses Python, MPlayer, Mencoder, DVDAuthor,
VCDImager, and mkisofs, so it has very few dependencies.

%prep
%setup -q

%build

%install
rm -rf %buildroot
DESTDIR=%buildroot \
prefix=%_prefix \
libdir=%_libdir \
	./install.sh

# fd.o icons - AdamW 2007/06
mkdir -p %buildroot%_iconsdir/hicolor/{16x16,32x32,48x48,x64x64}/apps
mv %buildroot%_datadir/pixmaps/%{name}.png %buildroot%_iconsdir/hicolor/64x64/apps/%{name}.png
convert -scale 48 %buildroot%_iconsdir/hicolor/64x64/apps/%{name}.png %buildroot%_iconsdir/hicolor/48x48/apps/%{name}.png
convert -scale 32 %buildroot%_iconsdir/hicolor/64x64/apps/%{name}.png %buildroot%_iconsdir/hicolor/32x32/apps/%{name}.png
convert -scale 16 %buildroot%_iconsdir/hicolor/64x64/apps/%{name}.png %buildroot%_iconsdir/hicolor/16x16/apps/%{name}.png

%find_lang %name

%post
%update_menus
%update_icon_cache hicolor

%postun
%clean_menus
%clean_icon_cache hicolor

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(0755,root,root,0755)
%_bindir/devede
%defattr(0644,root,root,0755)
%_datadir/applications/devede.desktop
%_datadir/devede
%_datadir/doc/devede
%_iconsdir/hicolor/64x64/apps/%{name}.png
%_iconsdir/hicolor/48x48/apps/%{name}.png
%_iconsdir/hicolor/32x32/apps/%{name}.png
%_iconsdir/hicolor/16x16/apps/%{name}.png
%_libdir/devede
