Summary:	Dockable APM/Battery Monitor for WindowMaker/AfterStep
Summary(pl):	Dokowalny monitor APM dla WindowMakera/AfterStepa
Name:		wmbattery
Version:	1.1
Release:	1
Group:          X11/Window Managers/Tools
Group(pl):      X11/Zarz±dcy Okien/Narzêdzia
Copyright:	GPL
Source:		http://kitenet.net/programs/wmbattery/%{name}.tar.gz
Patch:		wmbattery-makefile.patch
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot:   	/tmp/%{name}-%{version}-root

%description
WMBattery displays the status of your laptop's battery in a small
icon. This includes if it is plugged in, if the battery is charging,
how many minutes of battery life remain, battery life remaining (with 
both a percentage and a graph), and battery status (high - green, 
low - yellow, or critical - red).

%description -l pl
WMBattery wy¶wietla informacje dotycz±ce stanu baterii laptopa,
rodzaj wykorzystywanego ¼ród³a energii, d³ugo¶æ ¿ycia baterii,
czas pozosta³y do wyczerpania baterii, stan obci±¿enia baterii, itp.

%prep
%setup -q
%patch -p0

%build
make OPTS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

make install PREFIX=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/share/man/man1/* \
	README TODO debian/changelog debian/copyright

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO,debian/changelog,debian/copyright}.gz
%attr(755,root,root) /usr/X11R6/bin/wmbattery

/usr/X11R6/share/man/man1/*
/usr/X11R6/share/wmbattery

%changelog
* Sat May  8 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.1-1]
- initial rpm release for PLD.
