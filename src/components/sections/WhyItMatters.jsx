
import React from "react"
import { motion } from "framer-motion"

export default function WhyItMatters() {
  return (
    <section className="py-20">
      <div className="container mx-auto px-4 max-w-3xl text-center">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
        >
          <h2 className="text-3xl font-bold mb-8 text-gradient">Why It Matters</h2>
          <p className="text-xl md:text-2xl leading-relaxed text-muted-foreground">
            Moments don't just happen — they're felt.<br />
            Vibelytics helps artists and producers understand what truly moved their audience, 
            without ever compromising privacy.<br />
            Because in live entertainment, the vibe is everything.
          </p>
        </motion.div>
      </div>
    </section>
  )
}
