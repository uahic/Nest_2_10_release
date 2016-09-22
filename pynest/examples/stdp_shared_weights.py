import nest

a = nest.Create('iaf_neuron')
b = nest.Create('iaf_neuron')
c = nest.Create('iaf_neuron')

nest.Connect(a, c, 'one_to_one', {'model': 'stdp_synapse_shared', 'weight': 20.0})
nest.Connect(b, c, 'one_to_one', {'model': 'stdp_synapse_shared', 'weight': 31.0})

gen = nest.Create('poisson_generator')
nest.SetStatus(gen, 'rate', 100000.0)

nest.Connect(gen, c, 'one_to_one')
nest.Connect(gen, a, 'one_to_one')
nest.Connect(gen, b, 'one_to_one')


# Let both synapses share a single weight (label: 'L1')
syn_a_c = nest.GetConnections(source=a, target=c)
nest.SetStatus(syn_a_c, 'label', 'L1')

syn_b_c = nest.GetConnections(source=b, target=c)
nest.SetStatus(syn_b_c, 'label', 'L')
print nest.GetStatus(syn_b_c)

for i in xrange(2):
    nest.Simulate(1000.0)
    print nest.GetStatus(syn_a_c, 'weight'), nest.GetStatus(syn_b_c, 'weight')

# Further simulation while allowing the connection b->c having its own weight
# (label: 'L2')
nest.SetStatus(syn_b_c, 'label', 'L2')
for i in xrange(2):
    nest.Simulate(1000.0)
    print nest.GetStatus(syn_a_c, 'weight'), nest.GetStatus(syn_b_c, 'weight')

