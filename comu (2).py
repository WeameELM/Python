#!/usr/bin/python

#1
def cree_reseau(t_amis):
    """
    ajoute un dictionnaire les couples en les séparant par personne
    et en remplissant leurs amis
    """ 
    reseau = {}
    for amis1, amis2 in t_amis:
        if amis1 not in reseau:
            reseau[amis1] = []
        if amis2 not in reseau:
            reseau[amis2] = []
        reseau[amis1].append(amis2)
        reseau[amis2].append(amis1)
    return reseau

#3
def liste_personne(reseau):
    """
    renvoie la liste distincte des personne du reseau sous la forme de tableau 
    """
    liste = []
    for personne in reseau:
        if personne not in liste:
            liste.append(personne)
    return liste

#4
def sont_amis(reseau, personne1, personne2):
    """
    renvoie booléen, teste si deux personnes (en paramètres) sont amis 
    """
    if personne2 not in reseau[personne1]:
        return False
    return True

#5
def sont_amis_de(personne1, groupe, reseau):
    """
    teste si tous les membres d'un groupe (en paramètres) sont amis 
    """
    for personne2 in groupe:
        if not sont_amis(reseau, personne1, personne2) and personne2 != personne1:
            return False
    return True

#6
def est_commu(groupe, reseau):
    """ 
    teste si un groupe de personne est une communauté, renvoie un booléen 
    """
    for personne in groupe:
        for personne2 in groupe:
            if personne2 != personne and personne2 not in reseau[personne]:
                return False
    return True

#7
def commu(groupe, reseau):
    """
    renvoie une communauté formé seulement si la personne amie avec elle d'avant à partir de la première personne
    à partir d'un groupe 
    """
    commu = []
    for personne in groupe:
        if sont_amis_de(personne, commu, reseau):
            commu.append(personne)
    return commu

def echange(t, i, j):
    tmp = t[i]
    t[i] = t[j]
    t[j] = tmp
    return t

def nombre_amis(reseau, personne):
    for amis in reseau:
        if amis == personne:
            nombre_amis = len(reseau[amis])
    return nombre_amis

#8
def tri_popu(reseau, groupe):
    """
    tri du groupe d'ami selon l'odre décroissant, renvoie un tableau
    """
    n = len(groupe)
    nt = 1
    while nt < n:
        i = n - nt
        while i < n and nombre_amis(reseau, groupe[i-1]) < nombre_amis(reseau, groupe[i]):
            echange(groupe, i-1, i)
            i += 1
        nt += 1
    return groupe

#9
def commu_dans_reseau(reseau):
    """
    renvoie une communauté formé à partir du réseau
    """
    les_plus_pop = tri_popu(reseau, liste_personne(reseau))
    les_plus_pop_commu = commu(les_plus_pop, reseau)
    return les_plus_pop_commu

#10
def comu_dans_amis(reseau, personne):
    """
    part d'une personne et construit sa communauté à partir du réseau, renvoie un tableau 
    """
    commu = [personne]
    ami_trie = tri_popu(reseau, reseau[personne])
    for ami in ami_trie:
        if sont_amis_de(ami, ami_trie, reseau):
            commu.append(ami)
    return commu

#12
def commu_max(reseau):
    """
    renvoie la plus grande communauté dans un réseau, renvoie un tableau 
    """
    max_commu = []
    for personne in reseau:
        commu = comu_dans_amis(reseau, personne)
        if len(commu) > len(max_commu):
            max_commu = commu
    return max_commu
