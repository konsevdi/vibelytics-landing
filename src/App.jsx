
import React from "react"
import { motion } from "framer-motion"
import { Button } from "@/components/ui/button"
import { Toaster } from "@/components/ui/toaster"
import { Mail, Twitter, Instagram as TikTok } from 'lucide-react'
import Header from "@/components/Header"
import ParticleField from "@/components/ParticleField"
import SignupDialog from "@/components/SignupDialog"

export default function App() {
  return (
    <div className="min-h-screen bg-background">
      <ParticleField />
      <Toaster />
      <Header />
      
      {/* Hero Section */}
      <section className="min-h-screen flex items-center justify-center pt-20 pb-32 relative overflow-hidden">
        <div className="container mx-auto px-4 text-center relative z-10">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
          >
            <h1 className="text-5xl md:text-7xl font-bold mb-6 text-gradient">
              Vibelytics: The Emotional Intelligence Layer for Live Entertainment
            </h1>
            <p className="text-xl md:text-2xl text-muted-foreground mb-12 max-w-3xl mx-auto">
              Real-time emotional insight — no phones, no surveys, no surveillance.
            </p>
            <SignupDialog />
          </motion.div>
        </div>
      </section>

      {/* What We Do Section */}
      <section className="py-32 relative">
        <div className="container mx-auto px-4">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="max-w-3xl mx-auto text-center"
          >
            <h2 className="text-4xl md:text-5xl font-bold mb-8 text-gradient">What We Do</h2>
            <p className="text-xl md:text-2xl leading-relaxed text-muted-foreground">
              Vibelytics helps artists, producers, and sponsors understand what truly moved the crowd — moment by moment.<br />
              We analyze crowd reactions using ethical AI to map emotional spikes across set-lists, activations, and show cues.<br />
              No phone tracking, no facial recognition, no personal-data storage
            </p>
          </motion.div>
        </div>
      </section>

      {/* How It Works Section */}
      <section className="py-32 relative">
        <div className="cmax-w-3xl mx-auto text-center">
          <h2 className="text-4xl md:text-5xl font-bold mb-8 text-gradient">How It Works</h2>
          <div className="grid md:grid-cols-3 gap-8">
            {[
              {
                title: "Today:",
                description: "Post-event insight reports powered by AI-based emotion detection on timestamped imagery."
              },
              {
                title: "Roadmap:",
                description: "Real-time overlays, video + audio integration, and adaptive crowd-feedback loops."
              },
              {
                title: "Built for scale:",
                description: "Privacy-first, CE-readiness roadmap, GDPR-aligned from day one."
              }
            ].map((step, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.2 }}
                className="p-8 rounded-2xl bg-black/20 backdrop-blur-sm border border-primary/20"
                whileHover={{
                  scale: 1.02,
                  transition: { duration: 0.2 }
                }}
              >
                <h3 className="text-2xl font-semibold mb-4">{step.title}</h3>
                <p className="text-lg text-muted-foreground">{step.description}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Ethics at the Core Section */}
      <section className="py-32 relative">
        <div className="container mx-auto px-4">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="max-w-3xl mx-auto text-center"
          >
            <h2 className="text-4xl md:text-5xl font-bold mb-8 text-gradient">Ethics at the Core</h2>
            <p className="text-xl md:text-2xl leading-relaxed text-muted-foreground">
              No surveillance. No identity tracking.<br />
              DPIA completed. CE-mark roadmap in progress.<br />
              Emotion insights designed for artistry and audience respect.
            </p>
          </motion.div>
        </div>
      </section>

      {/* Why It Matters Section */}
      <section className="py-32 relative">
        <div className="max-w-3xl mx-auto text-center">
          <h2 className="text-4xl md:text-5xl font-bold mb-8 text-gradient">Why It Matters</h2>
          <div className="grid md:grid-cols-3 gap-8">
            {[
              {
                title: "Artists:",
                description: "Know what landed, what moved your audience."
              },
              {
                title: "Producers:",
                description: "Optimize emotional flow, not just logistics."
              },
              {
                title: "Sponsors:",
                description: "Prove emotional impact — not just impressions."
              }
            ].map((step, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.2 }}
                className="p-8 rounded-2xl bg-black/20 backdrop-blur-sm border border-primary/20"
                whileHover={{
                  scale: 1.02,
                  transition: { duration: 0.2 }
                }}
              >
                <h3 className="text-2xl font-semibold mb-4">{step.title}</h3>
                <p className="text-lg text-muted-foreground">{step.description}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="min-h-screen flex items-center justify-center pt-20 pb-32 relative overflow-hidden">
        <div className="container mx-auto px-4 text-center relative z-10">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
          >
            <h1 className="text-4xl md:text-5xl font-bold mb-8 text-gradient">
              Pilots Have Started
            </h1>
            <p className="text-xl md:text-2xl text-muted-foreground mb-12 max-w-3xl mx-auto">
              We’re onboarding early partners for pilot deployments.<br />
              Get in touch to explore how emotion insights can elevate your next show.
            </p>
            <SignupDialog />
          </motion.div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-12 border-t border-primary/20 relative">
        <div className="container mx-auto px-4">
          <div className="flex flex-col md:flex-row justify-between items-center gap-6">
            <div className="flex items-center gap-6">
              <a href="mailto:yes@vibelytics.ai" className="flex items-center gap-2 text-muted-foreground hover:text-foreground transition-colors">
                <Mail size={20} />
                yes@vibelytics.ai
              </a>
              <a href="https://twitter.com/vibelyticsai" target="_blank" rel="noopener noreferrer" className="text-muted-foreground hover:text-foreground transition-colors">
                <Twitter size={20} />
              </a>
              <a href="https://tiktok.com/@vibelyticsai" target="_blank" rel="noopener noreferrer" className="text-muted-foreground hover:text-foreground transition-colors">
                <TikTok size={20} />
              </a>
            </div>
            <div className="text-sm text-muted-foreground">
              Built by <a href="https://keytio.com" target="_blank" rel="noopener noreferrer" className="hover:text-foreground transition-colors">Keytio</a>
            </div>
          </div>
        </div>
      </footer>
    </div>
  )
}
