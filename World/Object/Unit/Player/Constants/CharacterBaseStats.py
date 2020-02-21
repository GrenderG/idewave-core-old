from World.Object.Unit.Player.Constants.CharacterRace import CharacterRace
from World.Object.Unit.Player.Constants.CharacterClass import CharacterClass

# list index equals to character level
BASE_STATS = {
    CharacterClass.DRUID.value: {
        'agility': [
            15, 17, 18, 19, 19, 19, 20, 21, 23, 24, 26, 29, 31, 34, 36, 39, 41, 45, 47, 50, 52, 56, 58,
            62, 65, 67, 69, 73, 76, 78, 81, 83, 86, 90, 93, 95, 98, 100, 103, 106, 109, 111, 114, 116,
            120, 124, 126, 129, 131, 134, 136, 140, 142, 145, 147, 151, 153, 156, 158, 162, 173, 184,
            195, 198, 201, 204, 206, 209, 211, 222
        ],
        'intellect': [
            12, 13, 14, 15, 15, 15, 16, 17, 18, 19, 21, 23, 25, 27, 29, 31, 33, 36, 38, 40, 42, 45, 47, 50,
            52, 54, 56, 59, 61, 63, 65, 67, 69, 73, 75, 77, 79, 81, 83, 86, 88, 90, 92, 94, 97, 100, 102, 104,
            106, 108, 110, 113, 115, 117, 119, 122, 124, 126, 128, 131, 140, 149, 158,
            160, 163, 165, 167, 169, 171, 180
        ],
        'strength': [
            7, 8, 9, 9, 9, 9, 10, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22, 23, 24, 25, 27, 28, 30, 31, 33,
            34, 36, 37, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 52, 53, 54, 56, 57, 59, 60, 62, 63, 64, 65,
            66, 68, 69, 71, 72, 74, 75, 76, 77, 79, 84, 90, 95, 96, 98, 99, 101, 102, 103, 108
        ],
        'stamina': [
            11, 12, 12, 13, 13, 13, 14, 15, 16, 17, 18, 20, 22, 24, 25, 27, 29, 31, 33, 35, 36, 39, 41, 43, 45, 47,
            48, 51, 53, 54, 56, 58, 59, 63, 64, 66, 68, 70, 71, 74, 76, 77, 79, 81, 83, 86, 88, 89, 91, 93, 94, 97,
            99, 100, 102, 105, 106, 108, 110, 112, 120, 128, 135, 137, 140, 141, 143, 145, 146, 154
        ],
        'spirit': [
            9, 10, 11, 11, 11, 11, 12, 13, 14, 14, 16, 17, 19, 20, 22, 23, 25, 27, 29, 30, 32, 34, 35, 38, 39, 41,
            42, 44, 46, 47, 49, 50, 52, 55, 56, 58, 59, 61, 62, 65, 66, 68, 69, 71, 73, 75, 77, 78, 80, 81, 83, 85,
            86, 88, 89, 92, 93, 95, 96, 98, 105, 112, 119, 120, 122, 124, 125, 127, 128, 135
        ],
        'base_mana': [
            50, 50, 50, 50, 50, 50, 50, 120, 134, 149, 165, 182, 200, 219, 239, 260, 282, 305, 329, 354, 380, 392,
            420, 449, 479, 509, 524, 554, 584, 614, 629, 659, 689, 704, 734, 749, 779, 809, 824, 854, 869, 899,
            914, 944, 959, 989, 1004, 1019, 1049, 1064, 1079, 1109, 1124, 1139, 1154, 1169, 1199, 1214, 1229, 1244,
            1359, 1469, 1582, 1694, 1807, 1919, 2032, 2145, 2257, 2370
        ]
    },
    CharacterClass.HUNTER.value: {
        'agility': [
            15, 17, 18, 19, 19, 19, 20, 21, 23, 24, 26, 29, 31, 34, 36, 39, 41, 45, 47, 50, 52, 56, 58,
            62, 65, 67, 69, 73, 76, 78, 81, 83, 86, 90, 93, 95, 98, 100, 103, 106, 109, 111, 114, 116,
            120, 124, 126, 129, 131, 134, 136, 140, 142, 145, 147, 151, 153, 156, 158, 162, 173, 184, 195,
            198, 201, 204, 206, 209, 211, 222
        ],
        'intellect': [
            10, 11, 11, 12, 12, 12, 13, 14, 15, 16, 17, 19, 20, 22, 24, 25, 27, 29, 31, 33, 34, 37, 38, 41, 43,
            44, 46, 48, 50, 52, 53, 55, 57, 60, 61, 63, 65, 66, 68, 70, 72, 74, 75, 77, 79, 82, 84, 85, 87, 88,
            90, 93, 94, 96, 97, 100, 102, 103, 105, 107, 115, 122, 129, 131, 134, 135, 137, 138, 140, 147
        ],
        'strength': [
            10, 12, 12, 13, 13, 13, 14, 15, 16, 16, 18, 20, 21, 23, 25, 27, 29, 31, 33, 34, 36, 38, 40, 43,
            44, 46, 48, 51, 52, 54, 55, 57, 59, 62, 64, 66, 68, 69, 71, 74, 75, 77, 79, 80, 83, 85, 87, 89,
            90, 92, 94, 96, 98, 100, 102, 104, 106, 107, 109, 111, 119, 127, 135, 136, 139, 141, 142, 144, 146, 153
        ],
        'stamina': [
            11, 12, 12, 13, 13, 13, 14, 15, 16, 17, 18, 20, 22, 24, 25, 27, 29, 31, 33, 35, 36, 39, 41, 43, 45, 47,
            48, 51, 53, 54, 56, 58, 59, 63, 64, 66, 68, 70, 71, 74, 76, 77, 79, 81, 83, 86, 88, 89, 91, 93, 94, 97,
            99, 100, 102, 105, 106, 108, 110, 112, 120, 128, 135, 137, 140, 141, 143, 145, 146, 154
        ],
        'spirit': [
            8, 9, 10, 10, 10, 10, 11, 12, 13, 13, 15, 15, 17, 18, 20, 21, 23, 25, 26, 27, 29, 31, 32, 35, 35, 37,
            38, 40, 42, 43, 45, 45, 47, 50, 51, 53, 54, 55, 56, 59, 60, 62, 63, 65, 66, 68, 70, 71, 73, 74, 75, 77,
            78, 80, 81, 84, 85, 86, 87, 89, 95, 102, 108, 109, 111, 113, 114, 115, 116, 123
        ],
        'base_mana': [
            65, 65, 65, 98, 98, 98, 98, 166, 166, 166, 166, 166, 166, 298, 298, 298, 298, 298, 298, 298, 298, 298,
            298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 298, 1075, 1075, 1075, 1075,
            1075, 1075, 1075, 1075, 1075, 1075, 1075, 1075, 1075, 1075, 1075, 1075, 1075, 1075, 1075, 1075, 1075,
            1075, 1075, 2053, 2053, 2053, 2053, 2053, 2053, 2053, 2053, 3383
        ]
    },
    CharacterClass.MAGE.value: {
        'agility': [
            10, 12, 12, 13, 13, 13, 14, 15, 16, 17, 18, 20, 21, 24, 25, 27, 28, 31, 33, 35, 36, 39, 40, 43,
            45, 46, 48, 51, 53, 54, 56, 57, 60, 62, 64, 66, 68, 69, 71, 73, 75, 77, 79, 80, 83, 86, 87, 89,
            91, 93, 94, 97, 98, 100, 102, 105, 106, 108, 109, 112, 120, 127, 135, 137, 139, 141, 143, 145, 146, 154
        ],
        'intellect': [
            12, 13, 14, 15, 15, 15, 16, 17, 18, 19, 21, 23, 25, 27, 29, 31, 33, 36, 38, 40, 42, 45, 47, 50, 52,
            54, 56, 59, 61, 63, 65, 67, 69, 73, 75, 77, 79, 81, 83, 86, 88, 90, 92, 94, 97, 100, 102, 104, 106,
            108, 110, 113, 115, 117, 119, 122, 124, 126, 128, 131, 140, 149, 158, 160, 163, 165, 167, 169, 171, 180
        ],
        'strength': [
            8, 8, 9, 9, 9, 9, 10, 11, 12, 12, 13, 15, 16, 17, 18, 20, 21, 23, 24, 25, 26, 28, 29, 31, 32, 34, 35,
            37, 38, 39, 40, 42, 43, 45, 47, 48, 49, 51, 52, 54, 55, 56, 57, 59, 61, 62, 64, 65, 66, 67, 69, 70, 72,
            73, 74, 76, 77, 78, 80, 81, 87, 93, 98, 100, 101, 103, 104, 105, 106, 112
        ],
        'stamina': [
            11, 12, 12, 13, 13, 13, 14, 15, 16, 17, 18, 20, 22, 24, 25, 27, 29, 31, 33, 35, 36, 39, 41, 43, 45,
            47, 48, 51, 53, 54, 56, 58, 59, 63, 64, 66, 68, 70, 71, 74, 76, 77, 79, 81, 83, 86, 88, 89, 91, 93, 94,
            97, 99, 100, 102, 105, 106, 108, 110, 112, 120, 128, 135, 137, 140, 141, 143, 145, 146, 154
        ],
        'spirit': [
            13, 15, 16, 16, 16, 16, 18, 19, 21, 21, 24, 25, 28, 30, 33, 34, 37, 40, 43, 44, 47, 50, 52, 56, 58, 61,
            62, 65, 68, 69, 72, 74, 77, 81, 83, 86, 87, 90, 92, 96, 98, 100, 102, 105, 108, 111, 114, 115, 118, 120,
            123, 126, 127, 130, 131, 136, 137, 140, 142, 145, 155, 165, 176, 177, 180, 183, 185, 188, 189, 199
        ],
        'base_mana': [
            100, 110, 110, 110, 121, 121, 121, 121, 121, 196, 215, 215, 215, 263, 271, 295, 305, 331, 343, 371, 385,
            415, 431, 431, 431, 515, 515, 556, 592, 613, 634, 634, 634, 712, 733, 733, 733, 811, 811, 853, 853, 853,
            916, 916, 916, 916, 916, 1021, 1021, 1021, 1021, 1090, 1090, 1117, 1138, 1138, 1138, 1138, 1138, 1213,
            1213, 1213, 1521, 1521, 1521, 1521, 1932, 2035, 2035, 2241
        ]
    },
    CharacterClass.PALADIN.value: {
        'agility': [
            5, 6, 6, 7, 7, 7, 7, 7, 8, 9, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 18, 20, 21, 22, 23,
            24, 24, 26, 27, 28, 29, 29, 30, 32, 33, 34, 35, 35, 37, 38, 39, 39, 40, 41, 43, 44, 45, 46,
            46, 48, 48, 50, 50, 51, 52, 54, 54, 55, 56, 57, 61, 65, 69, 70, 71, 72, 73, 74, 75, 79
        ],
        'intellect': [
            12, 13, 14, 15, 15, 15, 16, 17, 18, 19, 21, 23, 25, 27, 29, 31, 33, 36, 38, 40, 42, 45, 47, 50, 52,
            54, 56, 59, 61, 63, 65, 67, 69, 73, 75, 77, 79, 81, 83, 86, 88, 90, 92, 94, 97, 100, 102, 104, 106,
            108, 110, 113, 115, 117, 119, 122, 124, 126, 128, 131, 140, 149, 158, 160, 163, 165, 167, 169, 171, 180
        ],
        'strength': [
            17, 19, 20, 21, 21, 21, 23, 24, 26, 27, 30, 33, 35, 38, 41, 44, 47, 51, 54, 56, 59, 63, 66, 70, 73,
            76, 79, 83, 86, 88, 91, 94, 97, 102, 105, 108, 111, 114, 116, 121, 123, 126, 129, 132, 136, 140, 143,
            146, 148, 151, 154, 158, 161, 164, 167, 171, 174, 176, 179, 183, 196, 208, 221, 224, 228,
            231, 234, 236, 239, 252
        ],
        'stamina': [
            11, 12, 12, 13, 13, 13, 14, 15, 16, 17, 18, 20, 22, 24, 25, 27, 29, 31, 33, 35, 36, 39, 41, 43, 45,
            47, 48, 51, 53, 54, 56, 58, 59, 63, 64, 66, 68, 70, 71, 74, 76, 77, 79, 81, 83, 86, 88, 89, 91, 93,
            94, 97, 99, 100, 102, 105, 106, 108, 110, 112, 120, 128, 135, 137, 140, 141, 143, 145, 146, 154
        ],
        'spirit': [
            9, 10, 11, 11, 11, 11, 12, 13, 14, 14, 16, 17, 19, 20, 22, 23, 25, 27, 29, 30, 32, 34, 35, 38, 39, 41,
            42, 44, 46, 47, 49, 50, 52, 55, 56, 58, 59, 61, 62, 65, 66, 68, 69, 71, 73, 75, 77, 78, 80, 81, 83, 85,
            86, 88, 89, 92, 93, 95, 96, 98, 105, 112, 119, 120, 122, 124, 125, 127, 128, 135
        ],
        'base_mana': [
            60, 64, 84, 90, 112, 120, 129, 154, 165, 192, 205, 219, 249, 265, 282, 315, 334, 354, 390, 412, 435, 459,
            499, 525, 552, 579, 621, 648, 675, 702, 729, 756, 798, 825, 852, 879, 906, 933, 960, 987, 1014, 1041,
            1068, 1110, 1137, 1164, 1176, 1203, 1230, 1257, 1284, 1311, 1338, 1365, 1392, 1419, 1446, 1458, 1485,
            1512, 1656, 1800, 1944, 2088, 2232, 2377, 2521, 2665, 2809, 2953
        ]
    },
    CharacterClass.PRIEST.value: {
        'agility': [
            12, 14, 15, 16, 16, 16, 17, 17, 19, 20, 22, 24, 26, 28, 30, 32, 34, 37, 39, 42, 43, 47,
            48, 52, 54, 56, 57, 61, 63, 65, 67, 69, 71, 75, 77, 79, 81, 83, 86, 88, 91, 92, 95, 96,
            100, 103, 105, 107, 109, 111, 113, 116, 118, 120, 122, 125, 127, 130, 131, 135, 144, 153,
            162, 165, 167, 170, 171, 174, 175, 184
        ],
        'intellect': [
            12, 13, 14, 15, 15, 15, 16, 17, 18, 19, 21, 23, 25, 27, 29, 31, 33, 36, 38, 40, 42, 45, 47, 50, 52,
            54, 56, 59, 61, 63, 65, 67, 69, 73, 75, 77, 79, 81, 83, 86, 88, 90, 92, 94, 97, 100, 102, 104, 106,
            108, 110, 113, 115, 117, 119, 122, 124, 126, 128, 131, 140, 149, 158, 160, 163, 165, 167, 169, 171, 180
        ],
        'strength': [
            10, 11, 12, 12, 12, 12, 13, 14, 15, 16, 17, 19, 20, 22, 24, 25, 27, 30, 31, 32, 34, 37, 38, 41, 42,
            44, 46, 48, 50, 51, 53, 54, 56, 59, 61, 63, 64, 66, 67, 70, 71, 73, 75, 76, 79, 81, 83, 85, 86, 87, 89,
            92, 93, 95, 97, 99, 101, 102, 104, 106, 114, 121, 128, 130, 132, 134, 136, 137, 138, 146
        ],
        'stamina': [
            11, 12, 12, 13, 13, 13, 14, 15, 16, 17, 18, 20, 22, 24, 25, 27, 29, 31, 33, 35, 36, 39, 41, 43, 45, 47,
            48, 51, 53, 54, 56, 58, 59, 63, 64, 66, 68, 70, 71, 74, 76, 77, 79, 81, 83, 86, 88, 89, 91, 93, 94, 97,
            99, 100, 102, 105, 106, 108, 110, 112, 120, 128, 135, 137, 140, 141, 143, 145, 146, 154
        ],
        'spirit': [
            9, 10, 11, 11, 11, 11, 12, 13, 14, 14, 16, 17, 19, 20, 22, 23, 25, 27, 29, 30, 32, 34, 35, 38, 39, 41,
            42, 44, 46, 47, 49, 50, 52, 55, 56, 58, 59, 61, 62, 65, 66, 68, 69, 71, 73, 75, 77, 78, 80, 81, 83, 85,
            86, 88, 89, 92, 93, 95, 96, 98, 105, 112, 119, 120, 122, 124, 125, 127, 128, 135
        ],
        'base_mana': [
            110, 119, 119, 119, 119, 119, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164,
            164, 164, 480, 480, 530, 530, 530, 530, 530, 530, 530, 530, 530, 530, 530, 530, 530, 530, 911, 911, 911,
            911, 911, 911, 911, 911, 911, 911, 911, 911, 911, 911, 911, 911, 911, 911, 911, 911, 911, 911, 911, 911,
            911, 911, 911, 911, 911, 911, 2620
        ]
    },
    CharacterClass.ROGUE.value: {
        'agility': [
            15, 17, 18, 19, 19, 19, 20, 21, 23, 24, 26, 29, 31, 34, 36, 39, 41, 45, 47, 50, 52, 56,
            58, 62, 65, 67, 69, 73, 76, 78, 81, 83, 86, 90, 93, 95, 98, 100, 103, 106, 109, 111, 114,
            116, 120, 124, 126, 129, 131, 134, 136, 140, 142, 145, 147, 151, 153, 156, 158, 162, 173,
            184, 195, 198, 201, 204, 206, 209, 211, 222
        ],
        'intellect': [
            8, 9, 10, 10, 10, 10, 11, 12, 12, 13, 14, 16, 17, 18, 20, 21, 23, 25, 26, 27, 29, 31, 32, 34, 35, 37,
            38, 40, 42, 43, 44, 46, 47, 50, 51, 53, 54, 55, 57, 59, 60, 61, 63, 64, 66, 68, 70, 71, 72, 74, 75,
            77, 78, 80, 81, 83, 85, 86, 87, 89, 96, 102, 108, 109, 111, 113, 114, 115, 117, 123
        ],
        'strength': [
            14, 16, 17, 17, 17, 17, 19, 20, 22, 22, 25, 27, 29, 31, 34, 36, 39, 42, 45, 46, 49, 52, 55, 58, 61,
            63, 65, 69, 71, 73, 75, 78, 80, 85, 87, 90, 92, 94, 96, 100, 102, 104, 107, 109, 113, 116, 119, 121,
            123, 125, 128, 131, 133, 136, 138, 142, 144, 146, 148, 152, 162, 172, 183, 186,
            189, 191, 194, 196, 198, 209
        ],
        'stamina': [
            11, 12, 12, 13, 13, 13, 14, 15, 16, 17, 18, 20, 22, 24, 25, 27, 29, 31, 33, 35, 36, 39, 41, 43, 45,
            47, 48, 51, 53, 54, 56, 58, 59, 63, 64, 66, 68, 70, 71, 74, 76, 77, 79, 81, 83, 86, 88, 89, 91, 93, 94,
            97, 99, 100, 102, 105, 106, 108, 110, 112, 120, 128, 135, 137, 140, 141, 143, 145, 146, 154
        ],
        'spirit': [
            6, 7, 8, 8, 8, 8, 8, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 20, 22, 23, 24, 26, 27, 28, 29, 30,
            31, 32, 33, 34, 35, 38, 38, 40, 40, 42, 42, 44, 45, 46, 47, 48, 50, 51, 53, 53, 55, 55, 57, 58, 59, 60,
            61, 63, 63, 65, 65, 67, 72, 76, 81, 82, 83, 85, 85, 87, 87, 92
        ]
    },
    CharacterClass.SHAMAN.value: {
        'agility': [
            15, 17, 18, 19, 19, 19, 20, 21, 23, 24, 26, 29, 31, 34, 36, 39, 41, 45, 47, 50, 52, 56,
            58, 62, 65, 67, 69, 73, 76, 78, 81, 83, 86, 90, 93, 95, 98, 100, 103, 106, 109, 111, 114,
            116, 120, 124, 126, 129, 131, 134, 136, 140, 142, 145, 147, 151, 153, 156, 158, 162, 173,
            184, 195, 198, 201, 204, 206, 209, 211, 222
        ],
        'intellect': [
            12, 13, 14, 15, 15, 15, 16, 17, 18, 19, 21, 23, 25, 27, 29, 31, 33, 36, 38, 40, 42, 45, 47, 50, 52,
            54, 56, 59, 61, 63, 65, 67, 69, 73, 75, 77, 79, 81, 83, 86, 88, 90, 92, 94, 97, 100, 102, 104, 106,
            108, 110, 113, 115, 117, 119, 122, 124, 126, 128, 131, 140, 149, 158, 160, 163, 165, 167, 169, 171, 180
        ],
        'strength': [
            7, 8, 9, 9, 9, 9, 10, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22, 23, 24, 25, 27, 28, 30, 31, 33, 34,
            36, 37, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 52, 53, 54, 56, 57, 59, 60, 62, 63, 64, 65, 66, 68,
            69, 71, 72, 74, 75, 76, 77, 79, 84, 90, 95, 96, 98, 99, 101, 102, 103, 108
        ],
        'stamina': [
            11, 12, 12, 13, 13, 13, 14, 15, 16, 17, 18, 20, 22, 24, 25, 27, 29, 31, 33, 35, 36, 39, 41, 43, 45, 47,
            48, 51, 53, 54, 56, 58, 59, 63, 64, 66, 68, 70, 71, 74, 76, 77, 79, 81, 83, 86, 88, 89, 91, 93, 94, 97,
            99, 100, 102, 105, 106, 108, 110, 112, 120, 128, 135, 137, 140, 141, 143, 145, 146, 154
        ],
        'spirit': [
            9, 10, 11, 11, 11, 11, 12, 13, 14, 14, 16, 17, 19, 20, 22, 23, 25, 27, 29, 30, 32, 34, 35, 38, 39, 41,
            42, 44, 46, 47, 49, 50, 52, 55, 56, 58, 59, 61, 62, 65, 66, 68, 69, 71, 73, 75, 77, 78, 80, 81, 83, 85,
            86, 88, 89, 92, 93, 95, 96, 98, 105, 112, 119, 120, 122, 124, 125, 127, 128, 135
        ],
        'base_mana': [
            55, 55, 55, 55, 55, 55, 121, 121, 121, 175, 190, 206, 223, 241, 260, 280, 301, 323, 346, 370, 395, 421,
            448, 476, 505, 535, 566, 598, 631, 665, 699, 733, 767, 786, 820, 854, 888, 922, 941, 975, 1009, 1028,
            1062, 1096, 1115, 1149, 1183, 1202, 1236, 1255, 1289, 1313, 1342, 1376, 1395, 1414, 1448, 1467, 1501,
            1520, 1664, 1808, 1951, 2095, 2239, 2383, 2527, 2670, 2814, 2958
        ]
    },
    CharacterClass.WARLOCK.value: {
        'agility': [
            12, 13, 14, 15, 15, 15, 15, 16, 18, 18, 20, 22, 24, 26, 28, 30, 31, 35, 36, 38, 40, 43,
            45, 48, 50, 51, 53, 56, 58, 60, 62, 64, 66, 69, 71, 73, 75, 77, 79, 81, 84, 85, 87, 89,
            92, 95, 97, 99, 101, 103, 104, 107, 109, 111, 113, 116, 117, 120, 121, 124, 133, 141, 150,
            152, 154, 157, 158, 160, 162, 170
        ],
        'intellect': [
            12, 13, 14, 15, 15, 15, 16, 17, 18, 19, 21, 23, 25, 27, 29, 31, 33, 36, 38, 40, 42, 45, 47, 50, 52,
            54, 56, 59, 61, 63, 65, 67, 69, 73, 75, 77, 79, 81, 83, 86, 88, 90, 92, 94, 97, 100, 102, 104, 106,
            108, 110, 113, 115, 117, 119, 122, 124, 126, 128, 131, 140, 149, 158, 160, 163, 165, 167, 169, 171, 180
        ],
        'strength': [
            6, 7, 8, 8, 8, 8, 9, 9, 10, 10, 11, 13, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 27, 28, 29, 30,
            31, 33, 33, 34, 36, 37, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58, 60, 61,
            62, 63, 65, 66, 67, 68, 69, 74, 79, 84, 85, 86, 88, 89, 89, 91, 96
        ],
        'stamina': [
            11, 12, 12, 13, 13, 13, 14, 15, 16, 17, 18, 20, 22, 24, 25, 27, 29, 31, 33, 35, 36, 39, 41, 43, 45, 47,
            48, 51, 53, 54, 56, 58, 59, 63, 64, 66, 68, 70, 71, 74, 76, 77, 79, 81, 83, 86, 88, 89, 91, 93, 94, 97,
            99, 100, 102, 105, 106, 108, 110, 112, 120, 128, 135, 137, 140, 141, 143, 145, 146, 154
        ],
        'spirit': [
            13, 15, 16, 16, 16, 16, 18, 19, 21, 21, 24, 25, 28, 30, 33, 34, 37, 40, 43, 44, 47, 50, 52, 56, 58, 61,
            62, 65, 68, 69, 72, 74, 77, 81, 83, 86, 87, 90, 92, 96, 98, 100, 102, 105, 108, 111, 114, 115, 118, 120,
            123, 126, 127, 130, 131, 136, 137, 140, 142, 145, 155, 165, 176, 177, 180, 183, 185, 188, 189, 199
        ],
        'base_mana': [
            90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90,
            90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 965, 965, 1022, 1022, 1022, 1022, 1022,
            1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022, 1522, 1522, 1522, 1522, 1522, 1522,
            1522, 1522, 1522, 1522, 2871
        ]
    },
    CharacterClass.WARRIOR.value: {
        'agility': [
            10, 12, 12, 13, 13, 13, 14, 15, 16, 17, 18, 20, 21, 24, 25, 27, 28, 31, 33, 35, 36, 39,
            40, 43, 45, 46, 48, 51, 53, 54, 56, 57, 60, 62, 64, 66, 68, 69, 71, 73, 75, 77, 79, 80,
            83, 86, 87, 89, 91, 93, 94, 97, 98, 100, 102, 105, 106, 108, 109, 112, 120, 127, 135,
            137, 139, 141, 143, 145, 146, 154
        ],
        'intellect': [
            8, 9, 10, 10, 10, 10, 11, 12, 12, 13, 14, 16, 17, 18, 20, 21, 23, 25, 26, 27, 29, 31, 32, 34, 35,
            37, 38, 40, 42, 43, 44, 46, 47, 50, 51, 53, 54, 55, 57, 59, 60, 61, 63, 64, 66, 68, 70, 71, 72,
            74, 75, 77, 78, 80, 81, 83, 85, 86, 87, 89, 96, 102, 108, 109, 111, 113, 114, 115, 117, 123
        ],
        'strength': [
            17, 19, 20, 21, 21, 21, 23, 24, 26, 27, 30, 33, 35, 38, 41, 44, 47, 51, 54, 56, 59, 63, 66, 70, 73,
            76, 79, 83, 86, 88, 91, 94, 97, 102, 105, 108, 111, 114, 116, 121, 123, 126, 129, 132, 136, 140, 143,
            146, 148, 151, 154, 158, 161, 164, 167, 171, 174, 176, 179, 183, 196, 208,
            221, 224, 228, 231, 234, 236, 239, 252
        ],
        'stamina': [
            11, 12, 12, 13, 13, 13, 14, 15, 16, 17, 18, 20, 22, 24, 25, 27, 29, 31, 33, 35, 36, 39, 41, 43, 45, 47,
            48, 51, 53, 54, 56, 58, 59, 63, 64, 66, 68, 70, 71, 74, 76, 77, 79, 81, 83, 86, 88, 89, 91, 93, 94, 97,
            99, 100, 102, 105, 106, 108, 110, 112, 120, 128, 135, 137, 140, 141, 143, 145, 146, 154
        ],
        'spirit': [
            8, 9, 10, 10, 10, 10, 10, 11, 12, 12, 14, 15, 16, 17, 19, 20, 22, 23, 25, 26, 28, 30, 30, 33, 34, 36,
            36, 38, 40, 41, 43, 43, 45, 48, 49, 50, 51, 53, 54, 56, 57, 59, 60, 62, 63, 65, 67, 68, 69, 70, 72, 74,
            75, 76, 77, 80, 81, 82, 83, 85, 91, 97, 103, 104, 106, 108, 109, 110, 111, 117
        ]
    }
}


BASE_STATS_MOD = {

    # Alliance
    CharacterRace.HUMAN.value: {'agility': 0, 'intellect': 0, 'strength': 0, 'stamina': 0, 'spirit': 0},
    CharacterRace.DWARF.value: {'agility': -4, 'intellect': -1, 'strength': +5, 'stamina': 1, 'spirit': -1},
    CharacterRace.NIGHT_ELF.value: {'agility': +4, 'intellect': 0, 'strength': -4, 'stamina': 0, 'spirit': 0},
    CharacterRace.GNOME.value: {'agility': +2, 'intellect': +3, 'strength': -5, 'stamina': 0, 'spirit': 0},
    CharacterRace.DRAENEI.value: {'agility': -3, 'intellect': 0, 'strength': +1, 'stamina': 0, 'spirit': +2},

    # Horde
    CharacterRace.ORC.value: {'agility': -3, 'intellect': -3, 'strength': +3, 'stamina': +1, 'spirit': +2},
    CharacterRace.TROLL.value: {'agility': +2, 'intellect': -4, 'strength': +1, 'stamina': 0, 'spirit': +1},
    CharacterRace.UNDEAD.value: {'agility': -2, 'intellect': -2, 'strength': -1, 'stamina': 0, 'spirit': +5},
    CharacterRace.TAUREN.value: {'agility': -4, 'intellect': -4, 'strength': +5, 'stamina': +1, 'spirit': +2},
    CharacterRace.BLOOD_ELF.value: {'agility': +2, 'intellect': +3, 'strength': -3, 'stamina': 0, 'spirit': -2}
}