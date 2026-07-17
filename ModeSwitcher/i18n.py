# -*- coding: utf-8 -*-
"""介面翻譯（i18n）：UI 字串用英文當原文，附繁中譯文表，跟隨 Blender 語言。
  英文介面 → 英文；繁中／簡中介面 → 都顯示繁體（不出簡體）。
掛在專屬翻譯 context（避免「Object Mode」「Vertex」等通用字被 Blender 內建翻譯蓋掉）。
繁中同時掛四代碼：zh_HANT/zh_TW（繁）、zh_HANS/zh_CN（簡也顯示繁）。
"""
import bpy

I18N_CTX = "ModeSwitcher"

_ZH = {
    # 餅選單模式標籤
    "Object Mode": "物體模式",
    "Edit Mode": "編輯模式",
    "Vertex": "頂點",
    "Face": "面",
    "Edge": "邊",
    "Pose Mode": "姿態模式",
    "Vertex Paint": "頂點繪製",
    "Draw Mode": "繪製模式",
    "Sculpt Mode": "雕刻模式",
    "Weight Paint": "權重繪製",
    # 附加元件清單說明
    "Quickly switch edit modes with a pie menu in the 3D viewport; "
    "from Object Mode jump straight to vertex / edge / face":
        "在 3D 視窗用餅選單快速切換編輯模式；物件模式可一鍵直通點／線／面。",
}

_ZH_CTX = {(I18N_CTX, en): zh for en, zh in _ZH.items()}
translations_dict = {"zh_HANT": _ZH_CTX, "zh_TW": _ZH_CTX,
                     "zh_HANS": _ZH_CTX, "zh_CN": _ZH_CTX}


def _t(msgid):
    """把英文原文翻成目前介面語言（英文介面回傳原文）。"""
    return bpy.app.translations.pgettext_iface(msgid, I18N_CTX)
