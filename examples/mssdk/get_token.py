import json

from client.api import TokApi
from examples.contants import API_KEY, BASE_URL


def example(device_config: str, cookie: str, proxy: str):
    client = TokApi(API_KEY, base_url=BASE_URL)

    get_token_response = client.mssdk_get_token(device_config, cookie, proxy)

    device_config_dict = json.loads(device_config)
    device_config_dict['device_token'] = get_token_response.json()

    print(f'Token was updated on: {device_config_dict["device_token"]}')


if __name__ == "__main__":
    cookie = 'sessionid=793d9bd7c0f946a3a06ad202bfe10c4f;sessionid_ss=793d9bd7c0f946a3a06ad202bfe10c4f;install_id=7277943823588984609;store-country-code=gb;store-country-code-src=uid;store-idc=useast2a;ttreq=1$4396190abdcaca324311efaadc2ae0424b05db26;msToken=VA4TnDZFx1CRMp02EbpkEkOjVP3KDDOSivAB2g80TWMGSuUpQNpEfddK1HSA7VO7d9tg9UftpBW4_copQdokS4AYwbeoLfxh7AOsghwaVWNav5ZmjWLE;odin_tt=04efff12d7fb42f6367dfadfc80774284f48f79f26d1d56685bb02cf54272859ff30a878011c952535fc11739620070c81ff78bb1e2d2b3ba94cbe002d0eaf2c01fbaae340cc5dd3d31122d7aff6d8a5;passport_csrf_token=9c4758d985cd1174593f527919ca19e3;passport_csrf_token_default=9c4758d985cd1174593f527919ca19e3;tt-target-idc=useast2a;tt-target-idc-sign=j9sEdsqSG2mgVDk6s6KDNuLWDb_go8dtpopawqgJMQqYNRslwr6Fsx4JVFQmCjkol_uv2QDdXdR1VfI4HRLAjcX6QuaQllbNxgpTvPfbBxmdAeGI8hC8qVULdt6uTnzaiNMa37Z0y6i4UXp5-TjOUGgamjLWdZVuSsNRKC50Ke7f7izFVA_K8L9P5sN9itTBB6GR1WVCE6By7dozx292UpBbaP-gSP5_FRUbi4jAY6vmt2xvQi8efyOiuqz1LP1bcKnqgTL8_ZjfYHos5n5V9LmLBTqMLzer45eD54LIMg7tidqHeOU2aHNhGDgpW-I13qC10ZDSnhcMMpYBhs2EgfXGCR0wDR0w1466gFVaBpNZ31FH-n4B1iFVlI0SLDPjHKfZjyrleTVzQ8eKGcu8fLRbRaiN_hErDhooJEOEnqMwjE163qfD1z4_H4i9zUQ4BcPfVOJ-BJHzliPLYn5kSm9B8O3Xvu5Jub_mVxnPIihyDINV0hvZKu8_Es8YzeGp;reg-store-region=GB;cmpl_token=AgQQAPOYF-RPsLU-ndJC550Y_2HpV-qL_6ITYM1oKA;multi_sids=7277943947582063649%3A793d9bd7c0f946a3a06ad202bfe10c4f;sid_guard=793d9bd7c0f946a3a06ad202bfe10c4f%7C1694528445%7C15552000%7CSun%2C+10-Mar-2024+14%3A20%3A45+GMT;sid_tt=793d9bd7c0f946a3a06ad202bfe10c4f;uid_tt=3c17152a8b31f3a91017cf6dd448a51db122d9878331ff598d566d926620f8d0;uid_tt_ss=3c17152a8b31f3a91017cf6dd448a51db122d9878331ff598d566d926620f8d0'
    device_config = '{"openudid": "19f35eb784ca4bbe", "iid": "7277943823588984609", "device_id": "7277940573788751392", "dyn_seed": "", "dyn_version": -1, "device_token": "ACs7-j8D5dbljyuXxpvXKvLXh", "login_token": "03793d9bd7c0f946a3a06ad202bfe10c4f0262d546342bbde655fb62b798c034577b469ec48342495d18037c0f89af061ba27085b3e3a7142bb946bc039348b33e7f874dda5b88b7886463477c262a0af10a5dc0bfa03b19a65a5abda53589b994e91-CkBiMzI5YjZmOTYzNjcxZTAwNGI3N2MwMmYzNDY0NGE5OWQ0NmVlMjBkYWRiZGY1MDNmOTdkNTJhOWMwOWZhMjdl-2.0.0", "login_token_sign": "942f908d1b88dedadf6ad86bd6152015fb5e33b162dca91370e3d821fd8d7d35f6e388f63b3f7142a490202b194ae895de121f15ecc56d29efd85b0842cfbe6ec71703aeee48d130ba3517466eaa07b85c26671c3520c42479672aa2b039723cf04610ef1043305f1d572cdb901fa7ad58c87da32cdf6bde615c04612ea47091", "cmpl_token": "AgICA6AAFikrPEDsvf3umVda3C9b0jjSUKgtF-RPsLU-ndJC550Y_2HpV-qL_6ITYM1oKA", "x_bd_lanusk": "#IMO5pCMor7yQjhyZ/LNxFiGRKtda8lBli0Hksf8dH003cuErbwxdnXk14WkDztTODpbX2EDtO+Zatui8", "x_bd_lanusv": "0", "client_key": "", "kmsv": "", "region": "GB", "app_language": "en", "language": "en", "sys_region": "GB", "carrier_region": "GB", "op_region": "GB", "locale": "en-GB", "device_type": "HG680_FJ", "device_brand": "IndiHome", "device": "HG680", "cpu_support_64": "false", "host_abi": "armeabi-v7a", "resolution_width": "768", "resolution_height": "1184", "clientudid": "8944c842-b4b2-4992-ac4b-ec8cbc816020", "request_id": "696f30ca-ffcf-4d6c-a093-4a17040d4318", "ac2": "wifi5g", "cdid": "9e8b1b35-31f0-4275-bf9f-919d812823cb", "os_api": "30", "timezone_name": "Europe/London", "dpi": 320, "display_density": "xhdpi", "ac": "wifi", "os_version": "11", "timezone_offset": 3600, "mcc_mnc": "2351", "carrier_name": "EE", "carrier_region_v2": 235, "device_platform": "android", "install_time": 1693923627, "rom": "V12.5.22.0.RKUEUXM", "build_id": "AL5186-selene-build-20220815155641", "rom_compile_UTC": 1660550407, "rom_version": "RP1A.200720.011", "app_log_session_id": "57347ebe-e551-4555-a1a9-caa52ff3adae", "token_request_session_id": "698a4bd4-2e6f-4b53-8c57-6b562f99c974", "ram_total_size": 8528325871, "internal_storage_size": 128394705240, "internal_free_size": 42781772584, "sdcard_size": 34240615872, "drm_id": "gWVxJBRztgu6+cziPI75tYFLhJlOSN3BYwZXawW+YMI=", "boot_time_UTC": 1694182827, "wifi_ip": "1623696253", "wifi_gateway_ip": "192.168.1.200", "dns_list": "[\\"8.8.8.8\\",\\"1.1.1.1\\"]", "app_start_time": 1694526327, "storage_change": 1694096427, "package_path": "/data/app/~~cesPzuX_MCUqkbfd24EZlw==/com.zhiliaoapp.musically-Vx055u4DZaWhKcn2PHUY9g==/base.apk", "cpu_core_num": 8, "proc_name": "MT6769H", "cpu_max_frequency": "1800000", "cpu_min_frequency": "500000", "supported_commands": "fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm lrcpc dcpop asimddp", "board": "eos", "ro_product_name": "eos_eea", "platform_board": "mt6768", "launch_first_time": 1694510427719, "device_product": "HG680_FJ", "arch": "arm32", "libc_hash": 2522085115, "ro_build_tags": "release-keys", "fingerprint": "IndiHome/eos_eea/HG680:11/RP1A.200720.011/V12.5.22.0.RKUEUXM:user/release-keys", "ro_desc": "IndiHome HG680_FJ HG680 11 RP1A.200720.011 V12.5.22.0.RKUEUXM user release-keys"}'
    proxy = 'socks5://szaueank:b8ransyr26pj@216.173.74.78:5758'

    example(device_config, cookie, proxy)
