Summary:	Dockable APM/Battery Monitor for WindowMaker/AfterStep
Summary(pl):	Dokowalny monitor APM dla WindowMakera/AfterStepa
Name:		wmbattery
Version:	1.6
Release:	1
Group:          X11/Window Managers/Tools
Group(pl):      X11/Zarz�dcy Okien/Narz�dzia
Copyright:	GPL
Source0:	http://kitenet.net/programs/wmbattery/%{name}-%{version}.tar.gz
Source1:	wmbattery.desktop
Patch:		wmbattery-makefile.patch
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define 	_prefix		/usr/X11R6
%define 	_mandir		%{_prefix}/man
%define		_applnkdir	%{_datadir}/applnk

%description
WMBattery displays the status of your laptop's battery in a small
icon. This includes if it is plugged in, if the battery is charging,
how many minutes of battery life remain, battery life remaining (with 
both a percentage and a graph), and battery status (high - green, 
low - yellow, or critical - red).

%description -l pl
WMBattery wy�wietla informacje dotycz�ce stanu baterii laptopa,
rodzaj wykorzystywanego �r�d�a energii, d�ugo�� �ycia baterii,
czas pozosta�y do wyczerpania baterii, stan obci��enia baterii, itp.

%prep
%setup -q
%patch -p0

%build
make OPTS="$RPM_OPT_FLAGS" ICONDIR=%{_datadir}/wmbattery

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/DockApplets 

make install \
	PREFIX=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1 \
	ICONDIR=%{_datadir}/wmbattery
	
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README TODO debian/changelog debian/copyright

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO,debian/changelog,debian/copyright}.gz
%attr(755,root,root) %{_bindir}/wmbattery

%{_mandir}/man1/*
%{_datadir}/wmbattery

%{_applnkdir}/DockApplets/wmbattery.desktop
