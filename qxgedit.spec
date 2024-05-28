Name:		qxgedit
Version:	0.9.91
Release:	1
Summary:	Qt XG Editor
License:	GPLv2+
Group:		Sound/Midi
URL:		https://qxgedit.sourceforge.io/
Source0:	https://downloads.sourceforge.net/qxgedit/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(alsa)
BuildRequires:	cmake(Qt6)
BuildRequires:	qmake-qt6
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6Core)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:	pkgconfig(gig)

%description
QXGEdit is a Qt GUI for editing MIDI System Exclusive files
for XG devices (eg. Yamaha DB50XG).

%prep
%autosetup -p1

%build
%cmake \
        -DCONFIG_QT6=yes

%make_build

%install
%make_install -C build

# menu
desktop-file-install \
	--remove-key="X-SuSE-translate" \
	--remove-key="Version" \
	--set-key=Exec --set-value="%{name}" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/org.rncbc.qxgedit.desktop

%files
%doc ChangeLog README
%{_bindir}/%{name}
%{_libdir}/qt6/plugins/styles/libskulpturestyle.so
%{_datadir}/applications/org.rncbc.qxgedit.desktop
%{_datadir}/metainfo/org.rncbc.qxgedit.metainfo.xml
%{_datadir}/qxgedit
%{_iconsdir}/hicolor/32x32/apps/org.rncbc.qxgedit.png
%{_iconsdir}/hicolor/scalable/apps/org.rncbc.qxgedit.svg
%{_mandir}/man1/%{name}*.1*
%{_mandir}/*/man1/qxgedit.1.*
