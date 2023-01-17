from os import path

# Paths
DATA_DIR = path.join(path.dirname(path.abspath(__file__)), "..", "data/")
ESSAYS_DIR = DATA_DIR + "essays/"

# Data Files
ESSAYS = {
    "mice.csv",
    "rat.csv",
    "hepg2.csv"
}

CATEGORICAL_COLUMNS = list({
    'ESPÉCIE/LINHAGEM',
    'OUTRO_CRIOPROTETOR',
    'TIPO_DE_MEIO_DE_CULTURA',
    'TEMPO_DE_AVALIAÇÃO_DA_VIABILIDADE',
    'TESTE_DE_VIABILIDADE',
    "REFERÊNCIA"
})

NUMERICAL_COLUMNS = list({
    '%_DMSO',
    '%_SFB',
    '%_MEIO_DE_CULTURA',
    '%_OUTRO_CRIOPROTETOR',
    '%_SOLUÇÃO_TOTAL',
    '%_ANTES_DO_CONGELAMENTO',
    '%_APÓS_O_DESCONGELAMENTO',
    '%_QUEDA_DA_VIABILIDADE',
    'TREHALOSE',
    'GLICEROL',
    'SACAROSE',
    'GLICOSE',
    'MALTOSE',
    'LACTOSE',
    'RAFFINOSE',
    'MALTOTRIOSE',
    'MALTOTETRAOSE',
    'MALTOPENTAOSE',
    'MALTOEXAOSE',
    'MALTOHEPTAOSE',
    'ϒ-CYCLODEXTRIN',
    'DEXTRAN',
    'Di-rhamnolipids'
})
