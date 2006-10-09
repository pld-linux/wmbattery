Summary:	Dockable APM/Battery Monitor for WindowMaker/AfterStep
Summary(pl):	Dokowalny monitor APM dla WindowMakera/AfterStepa
Name:		wmbattery
Version:	2.22
Release:	1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://ftp.debian.org/debian/pool/main/w/wmbattery/%{name}_%{version}.tar.gz
# Source0-md5:	0dfc58537e29768b07b29e82933e6671
Source1:	%{name}.desktop
URL:		http://kitenet.net/programs/wmbattery/
BuildRequires:	XFree86-devel
BuildRequires:	apmd-devel
ExclusiveArch:	%{ix86} ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%setup -q -n %{name}

%build
%configure 
%{__make} \
	icondir="%{_datadir}/%{name}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}
install -d $RPM_BUILD_ROOT{%{_desktopdir}/docklets,%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.1x $RPM_BUILD_ROOT%{_mandir}/man1
install *.xpm $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO debian/changelog debian/copyright
%attr(755,root,root) %{_bindir}/wmbattery
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_desktopdir}/docklets/wmbattery.desktop
