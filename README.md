# **TicTacToe**

## Rádoby umělá inteligence v piškvorkách

## Prezentace: https://tinyurl.com/TicTacToeNichita

### Mnoho lidí se dnes zajímá o umělou inteligenci (AI) a to, jak může být použita k řešení různých problémů. Jeden z nejzajímavějších způsobů, jak si vyzkoušet, jak funguje umělá inteligence, je vytvořit jednoduchou verzi piškvorek, ve které umělá inteligence hraje proti hráči.

Cílem mého projektu bylo vytvořit umělou inteligenci, která by se dokázala postavit proti hráčům v piškvorkách a vždy je porazit. Pro dosažení tohoto cíle jsem se rozhodl využít algoritmus nazvaný Minimax, který je široce používán pro strategické hry, jako jsou právě piškvorky. Minimax algoritmus umožňuje umělé inteligenci vyhodnocovat různé tahy a jejich důsledky, a to až do určité hloubky stromu tahů. Díky tomu může nalézt nejlepší tah, který může na hracím poli zahrát.

V projektu jsem využil knihovnu Pygame na mnoha místech pro vykreslování a grafiku projektu. Pygame bylo klíčové pro vytvoření vizuálního prostředí hry a poskytlo mi potřebné prostředky pro interakci s uživatelem.

Prvním způsobem, jak jsem využil Pygame, bylo vytvoření hlavního okna hry. Pomocí této knihovny jsem mohl vytvořit okno s přesnými rozměry, ve kterém se hráči mohli pohybovat a interagovat s hracím polem. Mohl jsem také nastavit různé grafické prvky okna, jako je název okna, ikonu aplikace nebo pozadí.

Dalším využitím Pygame bylo vykreslení hracího pole. To mi umožnilo vytvořit prázdné hrací pole s danými rozměry a vykreslit ho na obrazovku. Dle jsem taky mohl nastavit barvu hracího pole, rozměry jednotlivých políček a různé grafické prvky, které zvýrazňovaly aktuální tahy hráčů.

Pokud hráč provedl tah, Pygame mi umožnilo vykreslit odpovídající symbol (křížek nebo kolečko) na příslušné místo na hracím poli. Díky tomu hráči mohli vizuálně sledovat průběh hry a vidět, jaké tahy provedli a jaké tahy provedla umělá inteligence.

Pygame bylo také použito pro vykreslení vizuálních prvků, které označovaly vítěze či remízu. Pokud došlo k výhře jednoho z hráčů, Pygame mi umožnilo vykreslit čáru přes vítěznou řadu symbolů na hracím poli, což jasně indikovalo, kdo vyhrál.

Celkově řečeno, Pygame bylo klíčovou knihovnou v projektu, která mi umožnila vytvořit atraktivní vizuální prostředí, vykreslit hrací pole, symboly hráčů a další grafické prvky, které zlepšily uživatelskou zkušenost a zábavnost hry.

Pro práci s daty jsem v projektu využil mocnou knihovnu NumPy. NumPy mi poskytl efektivní a flexibilní nástroje pro manipulaci s daty ve formě vícedimenzionálních polí.

Pomocí NumPy jsem vytvořil 2D pole, které přesně odpovídalo hracímu poli piškvorek. Toto pole mi sloužilo k ukládání informací o stavu hracího pole. Díky NumPy jsem mohl snadno sledovat, která políčka byla již zaškrtnuta hráči a která byla volná.
Mohl jsem také snadno přistupovat k jednotlivým prvkům pole, přiřazovat jim hodnoty a provádět různé operace, jako je kontrola, zda je pole prázdné nebo zda je dané políčko již zaškrtnuto.

Pro generování náhodných čísel jsem se spolehl na výkonnou a rozmanitou knihovnu Random. Ta mi umožnila vytvářet náhodné hodnoty pro různé aspekty hry, například pro výběr volného políčka, na které umělá inteligence zahraje.
Pro práci s hracím polem a zjištění dostupných tahů pro každou pozici jsem se obrátil k využití knihovny Copy. Tato knihovna mi poskytla efektivní způsob, jak provádět kopie hracího pole.

Díky knihovně Copy jsem byl schopen provádět hluboké kopie hracího pole, což znamená, že jsem vytvářel nezávislé kopie obsahující stejné hodnoty. Tímto jsem zajistil, že umělá inteligence mohla prozkoumat různé možnosti a experimentovat s tahy bez ohrožení původního hracího pole. To bylo klíčové pro správné fungování Minimax algoritmu, který se spoléhá na prozkoumávání stromové struktury tahů a vyhodnocování jejich hodnoty.

Na závěr jsem využil knihovnu Pyautogui pro ohlášení vítěze hry nebo remízy, a tak jsem mohl informovat hráče o výsledku hry pomocí grafického rozhraní.

Díky kombinaci těchto knihoven jsem vytvořil plně funkční piškvorkovou hru s umělou inteligencí, která dokáže hrát proti hráči a využívá algoritmus Minimax k nalezení nejlepšího tahu.

Hra začíná prvním tahem, který vždy vykoná hráč s křížkem. Pokud hrajete proti umělé inteligenci, vždy jste na prvním tahu a vybíráte si svůj tah. Po prvním tahu hráče má umělá inteligence již předepsané tahy, aby mohla rychleji reagovat. Od druhého tahu umělá inteligence používá Minimax algoritmus, který jí umožňuje nalézt nejlepší tah a označit ho na hracím poli. Hra se řídí klasickými pravidly piškvorek, což znamená, že končí, když hráč nebo umělá inteligence dosáhne na hracím poli tří křížků nebo koleček za sebou ve svislé, vodorovné nebo diagonální řadě.

Po skončení hry se vítěz označí čarou přes všechny tři kolečka nebo křížky, a pokud dojde k remíze, hra oznámí, že skončila a skončilo to remízou.

Hra disponuje také třemi spouštěči kláves: "E", "R" a "D". Při stisknutí klávesy "R" se hra resetuje, všechny křížky nebo kolečka zmizí a hra začíná od úplného záčátku.

Klávesa "E" slouží ke změně herního režimu z hráče proti umělé inteligenci na hráče proti dalšímu hráči, jinak řečeno „pvp“. Tuto změnu je však možné provést pouze tehdy, když hra ještě nezačala nebo již skončila.

Pokud zmáčknete klávesu "D", dojde ke změně obtížnosti umělé inteligence. Můžete změnit úroveň z neporazitelné obtížnosti na algoritmus, který náhodně vybírá tahy, nebo naopak z algoritmu, který náhodně vybírá tahy, na rádoby umělou inteligenci, kterou nikdo nemůže porazit. Tuto změnu je opět možné provést pouze tehdy, když hra ještě nezačala nebo teprve bude začínat a žádný hráč ještě nezahrál svůj tah.

V budoucnu by bylo možné projekt dále rozvíjet a implementovat další funkce, například zlepšené grafické rozhraní, které by mohlo být kompatibilní se všemi obrazovkami a všemi rozlišeními. Lze také přidat více variant umělé inteligence s různou mírou náhodnosti ve výběru tahů, protože ne vždy existuje pouze jedno správné řešení pro každý tah. Avšak současná verze algoritmu vybere tah který jako první zaznamená.

Projekt má velký potenciál pro další rozvoj a implementaci různých funkcí. Několik možností, které by se mohly do projektu integrovat, jsou například:

1. Lepší grafické rozhraní: Projekt by mohl být vizuálně vylepšen s použitím atraktivnějších grafických prvků, přechodových efektů a animací. To by přispělo k lepší uživatelské zkušenosti a zvýšilo přitažlivost hry.

2. Kompatibilita se všemi obrazovkami a rozlišeními: Momentálně by bylo vhodné projekt optimalizovat tak, aby fungoval na různých zařízeních s různými velikostmi obrazovky a rozlišeními. To by zajistilo, že uživatelé mohou hrát hru na svých zařízeních bez ohledu na jejich specifikace.

3. Více randomizovaná umělá inteligence: Aktuálně se umělá inteligence zaměřuje na nalezení nejbližšího správného tahu. Bylo by zajímavé přidat do projektu varianty umělé inteligence, které by vykazovaly větší míru náhodnosti ve výběru tahů. Tím by se hra stala méně předvídatelnou a hráč by se musel přizpůsobit různým strategiím umělé inteligence.

4. Zakomponování alfa-beta pruning: Přestože jsou piškvorky relativně jednoduchou hrou, implementace algoritmu alfa-beta pruning by mohla zlepšit výkon umělé inteligence a snížit časovou náročnost výpočtů. Alfa-beta pruning by umělé inteligenci umožnilo vynechat výpočet některých tahů, které neovlivní konečný výsledek hry.

5. Rozšíření herních režimů: Projekt by mohl být obohacen o další herní režimy, které by poskytovaly hráčům různé zážitky. Například by se mohl přidat režim s různými velikostmi hracího pole nebo režim, ve kterém hráči soutěží proti sobě ve více kolech. To by rozšířilo možnosti hry a umožnilo hráčům prozkoumat různé strategie a taktiky.

6. Nastavitelné obtížnosti umělé inteligence: Rozšíření projektu by mohlo zahrnovat možnost nastavení obtížnosti umělé inteligence na různé úrovně. Hráči by si mohli vybrat mezi snadným, středně obtížným a náročným režimem, přičemž každá úroveň by představovala jinou výpočetní inteligenci a strategickou schopnost.

Tyto nápady představují jen několik možností, jak projekt dále rozvíjet. Nicméně je zde spousta prostoru pro inovace a implementaci dalších funkcí, které by mohly značně zlepšit zábavnost, obtížnost a komplexnost hry.
