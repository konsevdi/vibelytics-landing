
import React from "react"
import { motion } from "framer-motion"

export default function Header() {
  return (
    <header className="centered top-0 left-0 right-0 z-50 header-blur">
      <div className="container mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          <motion.a 
            href="/"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.6 }}
          >
            <img 
              src="/vibelytics-logo.png"
              alt="Vibelytics"
              className="h-12 md:h-16"
            />
          </motion.a>
        </div>
      </div>
    </header>
  )
}
