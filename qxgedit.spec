Summary:	Qt XG Editor
Name:	qxgedit
Version:	1.0.1
Release:	1
License:	GPLv2+
Group:		Sound/Midi
Url:		https://qxgedit.sourceforge.io/
Source0:	https://downloads.sourceforge.net/qxgedit/%{name}-%{version}.tar.gz

BuildRequires:	cmake >= 3.15
BuildRequires:	desktop-file-utils
BuildRequires:git
BuildRequires:	qmake-qt6
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gig)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(rtmidi)
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	pkgconfig(xkbcommon-x11)

%description
QXGEdit is a Qt GUI for editing MIDI System Exclusive files for XG devices
(eg. Yamaha DB50XG).

%files
%doc ChangeLog README
%{_bindir}/%{name}
%{_libdir}/qt6/plugins/styles/libskulpturestyle.so
%{_datadir}/applications/org.rncbc.%{name}.desktop
%{_datadir}/metainfo/org.rncbc.%{name}.metainfo.xml
%{_datadir}/%{name}
%{_iconsdir}/hicolor/32x32/apps/org.rncbc.%{name}.png
%{_iconsdir}/hicolor/scalable/apps/org.rncbc.%{name}.svg
%{_mandir}/man1/%{name}*.1*
%{_mandir}/*/man1/%{name}.1.*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%cmake \
				-DCONFIG_QT6=yes \
				-DCONFIG_RTMIDI=no \
				-DCONFIG_WAYLAND=no

%make_build


%install
%make_install -C build

# Fix desktop file
desktop-file-edit \
	--remove-key="X-SuSE-translate" \
	--remove-key="Version" \
	--set-key=Exec --set-value="%{name}" \
	%{buildroot}%{_datadir}/applications/org.rncbc.%{name}.desktop
