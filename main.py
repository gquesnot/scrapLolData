import wrapper
from util.init_lol_watcher import initLolWatcher
from wrapper.lol_data_controller import LolDataController

if __name__ == '__main__':
    # init function with his default parameter
    # update: update if needed
    # forceUpdate: update evryTime
    # showLog : show print init / load
    dc = LolDataController(update=True, forceUpdate=False, showLog=True)

    # change jsonDownloadUrl in tftWrapper if new update and run the command below
    # dc.tft.downloadJson()

    # update if needed or forced and load all dataclasses , you can clean jsonData with param clean
    # dc.lol.load(clean=True)
    dc.lol.load()

    # load  all tft dataclasses
    dc.tft.load()


    # TODO: fix itemsCombined JSON
    lw = initLolWatcher()

    jsonSummoner = lw.summoner.by_name("euw1", "randomIron")
    summoner = dc.lolApi.getSummoner(jsonSummoner)
    print(summoner)
    match = lw.match.by_id("EUROPE", "EUW1_5551190982")
    match = dc.lolApi.getMatch(match)




    # TFT

    # Traits
    # for traitName, trait in dc.tft.traits.items():
    #     print(traitName, trait)

    # Items
    # for itemId, item in dc.tft.items.items():
    #     print(itemId, item)

    # Champions
    # for championName, champion in dc.tft.champions.items():
    #     print(championName, champion)

    # LOL

    # Champions
    # for champName, champion in dc.lol.champions.items():
    #     print(f"{champName}:", "\n    - ".join([skin.name for skin in champion.skins]))

    # Items from dragon json
    # for itemId, item in dc.lol.items.items():
    #     print(item.id, item.name)

    # Items combined
    # for itemId, itemCombined, in dc.lol.itemsCombined.items():
    #     print(itemCombined.id, itemCombined.name)

    # Runes
    # for runeId, rune in dc.lol.runes.items():
    #     print(runeId, rune)

    # Runes path
    # for runePathId, runePath in dc.lol.runesPath.items():
    #     print(runePathId)
    #     for path in runePath.runes:
    #
    #         for rune in path:
    #             print("    ",rune)
    #         print()
    # ProfilIcons
    # for profilIconId, profilIcon in dc.lol.profileIcons.items():
    #     print(profilIconId, profilIcon)

    #SummonerSpells
    # for summonerSpellName, summonerSpell in dc.lol.summonerSpells.items():
    #     print(summonerSpellName, summonerSpell)

    # Seasons
    # for seasonId, season in dc.lol.seasons.items():
    #     print(seasonId, season)

    # GameModes
    # for gameModeName, gameMode in dc.lol.gameModes.items():
    #     print(gameModeName, gameMode)

    # GameTypes
    # for gameTypeName, gameType in dc.lol.gameTypes.items():
    #     print(gameTypeName, gameType)

    # Maps
    # for mapId, map_ in dc.lol.maps.items():
    #     print(mapId, map_)

    #Queues
    # for queueId, queue in dc.lol.queues.items():
    #     print(queueId, queue)
