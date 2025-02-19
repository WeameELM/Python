#!/usr/bin/python




from comu import cree_reseau, liste_personne, sont_amis, sont_amis_de, est_commu, commu, tri_popu, commu_dans_reseau, est_commu,comu_dans_amis, commu_max



friends = { "Alice" : ["Bob", "Dan"], "Bob" : ["Alice","Carl", "Dan"], "Carl" :["Bob"], "Dan" : ["Alice", "Bob"] }

t = [ ["Alice", "Bob"], ["Bob", "Dan"], ["Carol", "Anne"], ["Anne", "Bob"]]



#1      
def test_cree_reseau():
    assert cree_reseau(t) == {'Alice': ['Bob'], 'Bob': ['Alice', 'Dan', 'Anne'], 'Dan': ['Bob'], 'Carol': ['Anne'], 'Anne': ['Carol', 'Bob']}
    print("Tout fonctionne")
test_cree_reseau()

#3
def test_liste_personne():
    assert liste_personne(friends) == ['Alice', 'Bob', 'Carl', 'Dan']
    print("Tout fonctionne")
test_liste_personne()  

#4
def test_sont_amis():
    assert sont_amis(friends, 'Alice', 'Bob')
    assert sont_amis(friends, 'Alice', 'Carl') == False
    print("Tout fonctionne")
test_sont_amis()

#5
def test_sont_amis_de():
    assert sont_amis_de('Alice', ['Bob', 'Dan'], friends)
    assert sont_amis_de('Alice', ['Bob', 'Carl'], friends) == False
    print("Tout fonctionne")
test_sont_amis_de()

#6
def test_est_commu():
    assert est_commu(["Alice","Bob","Dan"],friends)
    assert est_commu(["Alice","Bob","Carl"],friends) == False
    print("Tout fonctionne")
test_est_commu()    

#7
def test_commu():
    assert commu( ["Alice", "Bob", "Carl", "Dan"] ,friends) ==  ["Alice", "Bob", "Dan"]
    assert commu(   ["Carl", "Alice", "Bob", "Dan"]  ,friends) ==   ["Carl", "Bob"]
    print("Tout fonctionne")
test_commu()    

#8
def test_tri_popu():
    assert tri_popu(friends,["Alice", "Bob", "Carl"]) == ["Bob", "Alice", "Carl"]
    print("Tout fonctionne")
test_tri_popu()  

#9
def test_comu_dans_reseau():
    assert commu_dans_reseau(friends) ==  ["Bob", "Alice", "Dan"]
    print("Tout fonctionne")
test_comu_dans_reseau()

#10
def test_comu_dans_amis():
    assert comu_dans_amis(friends, "Carl") == ["Carl", "Bob"]
    assert comu_dans_amis(friends,"Alice") == ["Alice", "Bob", "Dan"]
    print("Tout fonctionne")
test_comu_dans_amis()

#12
def test_comu_max():
    assert commu_max(friends) == ["Alice", "Bob", "Dan"]
    print("Tout fonctionne")
test_comu_max()
