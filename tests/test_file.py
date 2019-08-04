"""File tests."""

from py2ch.file import File

ALLOWED_FILE_EXTENSIONS = (
    {  # JPG
        'displayname': '.jpg',
        'fullname': '.jpg',
        'height': 960,
        'md5': 'bfe4bfce24b39af38ad2f2ea3cb1d69f',
        'name': '15649199235490.jpg',
        'nsfw': 0,
        'path': '/b/src/201273988/15649199235490.jpg',
        'size': 191,
        'thumbnail': '/b/thumb/201273988/15649199235490s.jpg',
        'tn_height': 170,
        'tn_width': 170,
        'type': 1,
        'width': 960,
    }, {  # MP4
        'displayname': '3B50D3D1-88EF-4[...].MP4',
        'duration': '00:00:59',
        'duration_secs': 59,
        'fullname': '3B50D3D1-88EF-461E-B785-D558A7507C1A.MP4',
        'height': 480,
        'md5': 'd547131f831344660a08af53cefa1f27',
        'name': '15649184912390.mp4',
        'nsfw': 0,
        'path': '/b/src/201273988/15649184912390.mp4',
        'size': 3237,
        'thumbnail': '/b/thumb/201273988/15649184912390s.jpg',
        'tn_height': 220,
        'tn_width': 220,
        'type': 10,
        'width': 480,
    }, {  # PNG
        'displayname': ')(.png',
        'fullname': ')(.png',
        'height': 688,
        'md5': '0e6c35336dc08e427ffbcbe21738e707',
        'name': '15649395030070.png',
        'nsfw': 0,
        'path': '/b/src/201290489/15649395030070.png',
        'size': 332,
        'thumbnail': '/b/thumb/201290489/15649395030070s.jpg',
        'tn_height': 170,
        'tn_width': 136,
        'type': 2,
        'width': 552,
    }, {  # WEBM
        'displayname': '1550534704009.webm',
        'duration': '00:00:35',
        'duration_secs': 35,
        'fullname': '1550534704009.webm',
        'height': 720,
        'md5': 'a8077e56d68603e751740b8cc871e5b4',
        'name': '15649398951150.webm',
        'nsfw': 0,
        'path': '/b/src/201290489/15649398951150.webm',
        'size': 4029,
        'thumbnail': '/b/thumb/201290489/15649398951150s.jpg',
        'tn_height': 95,
        'tn_width': 170,
        'type': 6,
        'width': 1280,
    }, {  # MOV
        'displayname': '714BDBFF-7C2E-4[...].MOV',
        'duration': '00:00:47',
        'duration_secs': 47,
        'fullname': '714BDBFF-7C2E-4314-86BB-7772D1ECFC73.MOV',
        'height': 1334,
        'md5': 'c3c0126ec41670718aab651a1495b078',
        'name': '15649190009670.mp4',
        'nsfw': 0,
        'path': '/b/src/201273988/15649190009670.mp4',
        'size': 18598,
        'thumbnail': '/b/thumb/201273988/15649190009670s.jpg',
        'tn_height': 170,
        'tn_width': 95,
        'type': 10,
        'width': 750,
    },
)


def test_file_success():
    """Test successful work of File."""
    for file_info in ALLOWED_FILE_EXTENSIONS:
        file_instance = File(**file_info)

        assert file_instance.displayname == file_info.get('displayname')
        assert file_instance.duration == file_info.get('duration')
        assert file_instance.duration_secs == file_info.get('duration_secs')
        assert file_instance.fullname == file_info.get('fullname')
        assert file_instance.height == file_info.get('height')
        assert file_instance.md5 == file_info.get('md5')
        assert file_instance.name == file_info.get('name')
        assert file_instance.nsfw == file_info.get('nsfw')
        assert file_instance.path == file_info.get('path')
        assert file_instance.size == file_info.get('size')
        assert file_instance.thumbnail == file_info.get('thumbnail')
        assert file_instance.tn_height == file_info.get('tn_height')
        assert file_instance.tn_width == file_info.get('tn_width')
        assert file_instance.type == file_info.get('type')
        assert file_instance.width == file_info.get('width')

        for key in file_info:
            assert hasattr(file_instance, key)  # noqa: WPS421
