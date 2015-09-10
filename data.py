# campaign_code,name,variant,campaign_type,placement,campaign_section,office,territory_targeted,paid_organic,owner,long_description,is unique helper column 
codes_csv = """
twt_gu,global twitter,1,Twitter,,,UK,,,,@Guardian - Twitter,UNIQUE
fb_gu,global facebook,1,Facebook,,,UK,,,,The Guardian - Facebook ,UNIQUE
fb_us,us facebook,1,Facebook,,,US,US,,,Guardian US - Facebook,UNIQUE
soc_567,australia facebook,1,Facebook,,,AU,AU,,,Guardian Australia - Facebook ,UNIQUE
fb_cif,facebook cif,1,Facebook,,commentisfree,,,,,Comment is Free - Facebook,UNIQUE
EMCMONTXT5510I2,Money Talks,1,Email,,money,,,,,Money Talks,UNIQUE
ema_1046,Close up,1,Email ,,film,,,,,Close up,UNIQUE
EMCEDUEML1658,Crib sheet,1,Email,,education,,,,,Crib sheet,UNIQUE
EMCCRWEML1626,Crosswords,1,Email ,,crosswords,,,,,Crosswords,UNIQUE
ema_789,Fashion Statement,1,Email ,,fashion,,,,,Fashion Statement,UNIQUE
EMCENVEML1631,Green Light,1,Email ,,environment,,,,,Green Light,UNIQUE
EMCNEWEML6619I2,Guardian Today - UK,1,Email ,,,UK,UK,,,Guardian Today - UK,UNIQUE
ema_632,Guardian Today - AUS,1,Email ,,,US,US,,,Guardian Today - AUS,UNIQUE
ema_565,Guardian Today - USA,1,Email ,,,AU,AU,,,Guardian Today - USA,UNIQUE
EMCNEWEML1644,Guardian Weekly,1,Email ,,media,,,,,Guardian Weekly,UNIQUE
ema_546,Media Briefing,1,Email ,,media,,,,,Media Briefing,UNIQUE
EMCNEWEML1643,Metropolitan Lines,1,Email ,,politics,,,,,Metropolitan Lines,UNIQUE
EMCGBLEML1625,Poverty Matters,1,Email ,,global-development,,,,,Poverty Matters,UNIQUE
ema_630,SleeveNotes,1,Email ,,music,,,,,SleeveNotes,UNIQUE
EMCSOCEML657,Society Briefing,1,Email ,,society,,,,,Society Briefing,UNIQUE
EMCSPTEML866,The Breakdown,1,Email ,,sport,,,,,The Breakdown,UNIQUE
EMCFTBEML853,The Fiver,1,Email ,,football,,,,,The Fiver,UNIQUE
EMCTRVEML1657,The Flyer,1,Email ,,travel,,,,,The Flyer,UNIQUE
EMCARTEML6852,Art Weekly,1,Email ,,artanddesign,,,,,Art Weekly,UNIQUE
EMCBKSEML3964,Book Club,1,Email ,,books,,,,,Book Club,UNIQUE
EMCSPTEML942,The Spin,1,Email ,,sport,,,,,The Spin,UNIQUE
ema_792,AUS Politics,1,Email ,,politics,AU,AU,,,AUS Politics,UNIQUE
ema_827,Zip file,1,Email ,,technology,,,,,Zip file,UNIQUE
ema_1364,Best of Comment is Free,1,Email ,,commentisfree,,,,,Best of Comment is Free,UNIQUE
ema_861,Film Today,1,Email ,,film,,,,,Film Today,UNIQUE
ema_1731,Australia Morning Mail,1,Email ,,,AU,AU,,,Australia Morning Mail,UNIQUE
ema_1732,First Dog on the Moon,1,Email ,,commentisfree,AU,AU,,,First Dog on the Moon,UNIQUE
ema_2313,Best of Comment is Free - Australia,1,Email ,,commentisfree,AU,AU,,,Best of Comment is Free - Australia,UNIQUE
tmb_gu,Guardian Tumblr,1,Tumblr,,,,,,,The Guardian - Tumblr,UNIQUE
twt_tc,The Counted,1,Twitter,,,US,,,,@TheCounted - Twitter,UNIQUE
fb_tc,The Counted,,Facebook,,,US,,,,The Counted - Facebook,UNIQUE
soc_3157,gdncif,,Tumblr,,commentisfree,,,,,Cif - Tumblr,UNIQUE
soc_3156,gdnopinion,,Twitter,,commentisfree,,,,,@commentisfree - Twitter,UNIQUE
soc_568,GuardianAus,,Twitter,,,AU,AU,,,@GuardianAus - Twitter,UNIQUE
edit_2221,GuardianUs,,Twitter,,,US,US,,,@GuardianUS - Twitter,UNIQUE
twt_a-sport_b-ussports_c-us_g-1,GdnUSsports,,Twitter,,sport,US,US,,,@GdnUSSports - Twitter,UNIQUE
twt_a-cities_b-gdncities,gdncities,,Twitter,,cities,,,,,@GuardianCities - Twitter,UNIQUE
twt_books_b-gdnbooks,gdnbooks,,Twitter,,books,,,,,@GuardianBooks - Twitter,UNIQUE
twt_a-travel_b-gdntravel,gdntravel,,Twitter,,travel,,,,,@GuardianTravel - Twitter,UNIQUE
twt_business_b-gdnbiz,gdnbiz,,Twitter,,business,,,,,@BusinessDesk - Twitter,UNIQUE
twt_a-film_b-gdnfilm,gdnfilm,,Twitter,,film,,,,,@GuardianFilm - Twitter,UNIQUE
twt_a-environment_b-gdneco,gdneco,,Twitter,,environment,,,,,@GuardianEco - Twitter,UNIQUE
twt_a-media_b-gdnmedia,gdnmedia,,Twitter,,media,,,,,@MediaGuardian - Twitter,UNIQUE
twt_a-science_b-gdnscience,gdnscience,,Twitter,,science,,,,,@GuardianScience - Twitter,UNIQUE
twt_b-gdnnews,gdnnews,,Twitter,,,,,,,@GuardianNews - Twitter,UNIQUE
twt_a-music_b-gdnmusic,gdnmusic,,Twitter,,music,,,,,@GuardianMusic - Twitter,UNIQUE
twt_a-education_b-gdnedu,gdnedu,,Twitter,,education,,,,,@GuardianEdu - Twitter,UNIQUE
twt_a-world_b-gdnworld,gdnworld,,Twitter,,world,,,,,@GuardianWorld - Twitter,UNIQUE
twt_a-education_b-gdnstudents,gdnstudents,,Twitter,,education,,,,,@GdnStudents - Twitter,UNIQUE
twt_a-technology_b-gdntech,gdntech,,Twitter,,technology,,,,,@GuardianTech - Twitter,UNIQUE
twt_a-sport_b-gdnsport,gdnsport,,Twitter,,sport,,,,,@Guardian_Sport - Twitter,UNIQUE
twt_a-lifeandstyle_b-gdnlifeandstyle,gdnlifeandstyle,,Twitter,,lifeandstyle,,,,,@LifeandStyle - Twitter,UNIQUE
twt_b-gdnphotos,gdnphotos,,Twitter,,,,,,,@GuardianPhotos - Twitter,UNIQUE
twt_a-global-development_b-gdndevelopment,gdndevelopment,,Twitter,,global-development,,,,,@GdnDevelopment - Twitter,UNIQUE
twt_b-gdng2,gdng2,,Twitter,,,,,,,@GuardianG2 - Twitter,UNIQUE
twt_b-gdnguide,gdnguide,,Twitter,,,,,,,@GuideGuardian - Twitter,UNIQUE
twt_b-gdnweekly,gdnweekly,,Twitter,,,,,,,@GuardianWeekly - Twitter,UNIQUE
twt_a-money_b-gdnmoney,gdnmoney,,Twitter,,money,,,,,@GuardianMoney - Twitter,UNIQUE
twt_a-society_b-gdnsociety,gdnsociety,,Twitter,,society,,,,,@SocietyGuardian - Twitter,UNIQUE
twt_b-obsnewreview,ObsNewReview,,Twitter,,,,,,,@ObsNewReview - Twitter,UNIQUE
twt_a-lifeandstyle_b-gdnfamily,gdnfamily,,Twitter,,lifeandstyle,,,,,@GuardianFamily - Twitter,UNIQUE
twt_b-gdnweekend,gdnweekend,,Twitter,,,,,,,@GuardianWeekend - Twitter,UNIQUE
twt_a-culture_b-gdnculture,gdnculture,,Twitter,,culture,,,,,@GuardianCulture - Twitter,UNIQUE
twt_a-stage_b-gdnstage,gdnstage,,Twitter,,stage,,,,,@GuardianStage - Twitter,UNIQUE
twt_b-gdnscotland,GdnScotland,,Twitter,,uk-news,,,,,@GdnScotland - Twitter,UNIQUE
twt_b-gdnlibrary,gdnlibrary,,Twitter,,,,,,,@GuardianLibrary - Twitter,UNIQUE
twt_a-artanddesign_b-gdnartanddesign,gdnartanddesign,,Twitter,,artanddesign,,,,,@GdnArtandDesign - Twitter,UNIQUE
twt_b-obsmagazine,obsmagazine,,Twitter,,,,,,,@Obsmagazine - Twitter,UNIQUE
twt_a-childrens-books-site_b-gdnchildrenbks,GdnChildrensBks,,Twitter,,childrens-books-site,,,,,@GdnChildrenBks - Twitter,UNIQUE
twt_a-world_b-gdnafrica,gdnafrica,,Twitter,,world,,,,,@GuardianAfrica - Twitter,UNIQUE
twt_b-gdnwitness,gdnwitness,,Twitter,,,,,,,@GuardianWitness - Twitter,UNIQUE
twt_b-gdnreview,gdnreview,,Twitter,,,,,,,@GuardianReview - Twitter,UNIQUE
twt_b-gdnaudio,gdnaudio,,Twitter,,,,,,,@guardianaudio - Twitter,UNIQUE
twt_a-lifeandstyle_b-gdnfood,gdnfood,,Twitter,,lifeandstyle,,,,,@GuardianFood - Twitter,UNIQUE
twt_a-science_b-gdnsciblog,gdnsciblog,,Twitter,,science,,,,,@GuardianScibBog - Twitter,UNIQUE
twt_a-football_b-thefiver,thefiver,,Twitter,,football,,,,,@TheFiver - Twitter,UNIQUE
twt_b-gdnobits,gdnobits,,Twitter,,(defaults to null),,,,,@GuardianObits - Twitter,UNIQUE
twt_a-tv-and-radio_b-gdntv,gdntv,,Twitter,,tv-and-radio,,,,,@GuardianTv - Twitter,UNIQUE
twt_a-lifeandstyle_b-gdngardens,gdngardens,,Twitter,,lifeandstyle,,,,,@GuardianGardens - Twitter,UNIQUE
twt_a-media_b-mgmediamonkey,mgmediamonkey,,Twitter,,media,,,,,@MgMediaMonkey - Twitter,UNIQUE
twt_a-tv-and-radio_b-gdnradio,gdnradio,,Twitter,,tv-and-radio,,,,,@GdnRadio - Twitter,UNIQUE
twt_a-culture_b-gdnausculture_c-au_g-3,GdnAusCulture,,Twitter,,culture,AU,AU,,,@GdnAusCulture - Twitter,UNIQUE
twt_b-gdnvideo,gdnvideo,,Twitter,,,,,,,@GdnVideo - Twitter,UNIQUE
twt_a-politics_b-gdnukpolitics,gdnukpolitics,,Twitter,,politics,,,,,@GdnPolitics - Twitter,UNIQUE
twt_b-g2filmandmusic,G2FilmandMusic,,Twitter,,,,,,,@G2FilmandMusic - Twitter,UNIQUE
twt_b-gdnnortherner,GdnNortherner,,Twitter,,,,,,,@GdnNortherner - Twitter,UNIQUE
twt_a-fashion_b-gdnfashion,gdnfashion,,Twitter,,fashion,,,,,@GdnFashion - Twitter,UNIQUE
twt_b-gdndata,gdndata,,Twitter,,,,,,,@GdnData - Twitter,UNIQUE
twt_b-obstechmonthly,ObsTechMonthly,,Twitter,,,,,,,@ObsTechMonthly - Twitter,UNIQUE
twt_a-higher-education-network_b-gdnfe,gdnFE,,Twitter,,higher-education-network,,,,,@GdnFE - Twitter,UNIQUE
twt_a-sustainable-business_b-gdnsocent,gdnsocent,,Twitter,,sustainable-business,,,,,@GdnSocEnt - Twitter,UNIQUE
twt_a-public-leaders-network_b-gdnpublic,gdnpublic,,Twitter,,public-leaders-network,,,,,@GdnPublic - Twitter,UNIQUE
twt_a-higher-education_b-gdnhighered,GdnHigherEd,,Twitter,,higher-education,,,,,@GdnHigherEd - Twitter,UNIQUE
twt_a-sport_b-gdnausport_c-au_g-3,GdnAusSport,,Twitter,,sport,AU,AU,,,@GdnAusSport - Twitter,UNIQUE
twt_a-lifeandstyle_b-gdnstyle,gdnstyle,,Twitter,,lifeandstyle,,,,,@GuardianStyle - Twitter,UNIQUE
twt_a-gnm-archive_b-gdnarchive,GdnArchive,,Twitter,,gnm-archive,,,,,@GuardianArchive - Twitter,UNIQUE
twt_a-media-network_b-gdnmtn,gdnmtn,,Twitter,,media-network,,,,,@GdnMediaNetwork - Twitter,UNIQUE
twt_b-gdncountrydiary,gdncountrydiary,,Twitter,,,,,,,@GdnCountryDiary - Twitter,UNIQUE
twt_a-world_b-gdnnk,GdnNK,,Twitter,,world,,,,,@GdnNk - Twitter,UNIQUE
twt_a-world_b-gdnneweast,gdnNewEast,,Twitter,,world,,,,,@GdnNewEast - Twitter,UNIQUE
twt_a-music_b-gdnclassical,GdnClassical,,Twitter,,music,,,,,@GdnClassical - Twitter,UNIQUE
inst_a-cities_b-gdncities,gdncities,,Instagram,,cities,,,,,Cities Instagram,UNIQUE
inst_b-gdninsta,gdninsta,,Instagram,,,,,,,Guardian Instagram,UNIQUE
inst_a-travel_b-gdntravelsnaps,gdntravelsnaps,,Instagram,,travel,,,,,Travel Snaps Instagram,UNIQUE
inst_b-gdnus_c-us_g-1,gdnUS,,Instagram,,,US,US,,,Guardian US Instagram,UNIQUE
inst_b-gdnau_c-au_g-3,gdnAU,,Instagram,,,AU,AU,,,Guardian AUS Instagram,UNIQUE
inst_b-gdncam,gdncam,,Instagram,,,,,,,Guardian Cam Instagram,UNIQUE
fb_b-obsnewreview,obsnewreview,,Facebook,,,,,,,Observer New Review - Facebook,UNIQUE
fb_a-football_b-gdnfootball,gdnfootball,,Facebook,,football,,,,,Football - Facebook,UNIQUE
fb_a-culture_b-gdnculture,gdnculture,,Facebook,,culture,,,,,Culture - Facebook,UNIQUE
fb_a-technology_b-gdntech,gdntechn,,Facebook,,technology,,,,,Tech - Facebook,UNIQUE
fb_a-science_b-gdnscience,gdnscience,,Facebook,,science,,,,,Science - Facebook,UNIQUE
fb_a-media_b-gdnmedia,gdnmedia,,Facebook,,media,,,,,Media - Facebook,UNIQUE
fb_a-education_b-gdnedu,gdnedu,,Facebook,,education,,,,,Education - Facebook,UNIQUE
fb_a-music_b-gdnmusic,gdnmusic,,Facebook,,music,,,,,Music - Facebook,UNIQUE
fb_a-sport_b-gdnsport,gdnsport,,Facebook,,sport,,,,,Sport - Facebook,UNIQUE
fb_a-film_b-gdnfilm,gdnfilm,,Facebook,,film,,,,,Film - Facebook,UNIQUE
fb_a-society_b-gdnsociety,gdnscociety,,Facebook,,society,,,,,Society - Facebook,UNIQUE
fb_a-environment_b-gdnenvironment,gdnenvironment,,Facebook,,environment,,,,,Environment - Facebook,UNIQUE
fb_a-lifeandstyle_b-gdnlifeandstyle,gdnlifeandstyle,,Facebook,,lifeandstyle,,,,,Life and Style - Facebook,UNIQUE
fb_a-travel_b-gdntravel,gdntravel,,Facebook,,travel,,,,,Travel - Facebook,UNIQUE
fb_a-global-development_b-gdnglobaldev,gdnglobaldev,,Facebook,,global-development,,,,,Global Development - Facebook,UNIQUE
fb_b-gdndata,gdndata,,Facebook,,,,,,,Data - Facebook,UNIQUE
fb_a-fashion_b-gdnfashion,gdnfashion,,Facebook,,fashion,,,,,Fashion - Facebook,UNIQUE
fb_a-cities_b-gdncities,gdncities,,Facebook,,cities,,,,,Cities - Facebook,UNIQUE
fb_a-higher-education-network_b-gdnstudents,gdnstudents,,Facebook,,higher-education-network,,,,,Students - Facebook,UNIQUE
fb_a-teacher-network_b-gdnteachernetwork,gdnteachernetwork,,Facebook,,teacher-network,,,,,Teacher Network - Facebook,UNIQUE
fb_a-tv-and-radio_b-gdntvandradio,gdntvandradio,,Facebook,,tv-and-radio,,,,,TV and Radio - Facebook,UNIQUE
fb_a-books_b-gdnteenbooks,gdnteenbooks,,Facebook,,books,,,,,Books - Facebook,UNIQUE
fb_a-sport_b-gdnussport,gdnussport,,Facebook,,sport,,,,,US Sports - Facebook,UNIQUE
fb_b-gdnweekly,gdnweekly,,Facebook,,,,,,,Weekly - Facebook,UNIQUE
fb_a-technology_b-gdngames,gdngames,,Facebook,,technology,,,,,Games - Facebook,UNIQUE
fb_a-global-development-network_b-gdnglobaldevprofnetwork,gdnglobaldevprofnetwork,,Facebook,,global-development-professionals-network,,,,,Global Development Professional Network - Facebook,UNIQUE
fb_a-sustainable-business_b-gdnsustbiz,gdnsustbiz,,Facebook,,sustainable-business,,,,,Sustainable Business - Facebook,UNIQUE
fb_a-social-enterprise-network_b-gdnsocialenterprisenetwork,gdnsocialenterprisenetwork,,Facebook,,social-enterprise-network,,,,,Social Enterprise Network - Facebook,UNIQUE
fb_b-gdnwitness,gdnwitness,,Facebook,,,,,,,Witness - Facebook,UNIQUE
fb_a-higher-education_b-gdnhighereducationnetwork,gdnhighereducationnetwork,,Facebook,,higher-education,,,,,Higher Education Network - Facebook,UNIQUE
fb_a-culture-professionals-network_b-gdncultprofnetwork,gdncultprofnetwork,,Facebook,,culture-professionals-network,,,,,Culture Professionals Network - Facebook,UNIQUE
fb_a-media_b-gdnstudentmediaawards,gdnstudentmediaawards,,Facebook,,media,,,,,Student Media Awards - Facebook,UNIQUE
fb_a-voluntary-sector-network_b-gdnstudentmediaawards,gdnvoluntarysectornetwork,,Facebook,,voluntary-sector-network,,,,,Voluntary Sector Network - Facebook,UNIQUE
fb_a-healthcare-network_b-gdnhealthcarenetwork,gdnhealthcarenetwork,,Facebook,,healthcare-network,,,,,Healthcare Network - Facebook,UNIQUE
fb_a-small-business-network_b-gdnsmallbiznetwork,gdnsmallbiznetwork,,Facebook,,small-business-network,,,,,Small Business Network - Facebook,UNIQUE
fb_a-media-network_b-gdnmedianetwork,gdnmedianetwork,,Facebook,,media-network,,,,,Media Network - Facebook,UNIQUE
fb_a-housing-network_b-gdnhousingnetwork,gdnhousingnetwork,,Facebook,,housing-network,,,,,Housing Network - Facebook,UNIQUE
fb_a-culture_b-gdncultureau_c-au_g-3,gdncultureau,,Facebook,,culture,AU,AU,,,Culture Aus - Facebook,UNIQUE
tmb_a-music_b-gdnmusic,gdnmusic,,Tumblr,,music,,,,,Music - Tumblr,UNIQUE
tmb_b-english2english_c-us,English2English,,Tumblr,,,US,,,,English2English - Tumblr,UNIQUE
tmb_a-football_b-sadfootballers,SadFootballers,,Tumblr,,football,,,,,SadFootballers - Tumblr,UNIQUE
fb_b-firstdog_c-au_g-3,firstdog,,Facebook,,,AU,,,,First Dog on the Moon - Facebook,UNIQUE
twt_b-cifaus_c-au_g-3,cifaus,,Twitter,,commentisfree,AU,AU,,,@Cif_Australia - Twitter,UNIQUE
twt_b-realitycheck,realitycheck,,Twitter,,,,,,,@RealityCheck - Twitter,UNIQUE
"""
