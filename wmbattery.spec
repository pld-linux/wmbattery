Summary:	Dockable APM/Battery Monitor for WindowMaker/AfterStep
Summary(pl):	Dokowalny monitor APM dla WindowMakera/AfterStepa
Name:		wmbattery
Version:	1.6
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://kitenet.net/programs/code/wmbattery/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-makefile.patch
URL:		http://kitenet.net/programs/wmbattery/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define 	_mandir		%{_prefix}/man

%description
WMBattery displays the status of your laptop's battery in a small
icon. This includes if it is plugged in, if the battery is charging,
how many minutes of battery life remain, battery life remaining (with
both a percentage and a graph), and battery status (high - green, low
- yellow, or critical - red).

%description -l pl
WMBattery wy¶wietla informacje dotycz±ce stanu baterii laptopa, rodzaj
wykorzystywanego ¼ród³a energii, d³ugo¶æ ¿ycia baterii, czas pozosta³y
do wyczerpania baterii, stan obci±¿enia baterii, itp.

%prep
%setup -q
%patch -p0

%build
%{__make} OPTS="%{rpmcflags}" ICONDIR=%{_datadir}/wmbattery

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1 \
	ICONDIR=%{_datadir}/wmbattery

#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO debian/changelog debian/copyright
%attr(755,root,root) %{_bindir}/wmbattery
%{_mandir}/man1/*
%{_datadir}/wmbattery
#%{_applnkdir}/DockApplets/wmbattery.desktop
