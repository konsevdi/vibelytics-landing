
import React from "react"
import {
  Dialog,
  DialogContent,
  DialogTrigger,
} from "@/components/ui/dialog"
import { Button } from "@/components/ui/button"

export default function SignupDialog() {
  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button size="lg" className="text-lg px-8 py-6 glow">
          Get Early Access
        </Button>
      </DialogTrigger>
      <DialogContent className="p-0 border-none bg-transparent shadow-none">
        <iframe 
          src="https://signup.vibelytics.ai"
          className="w-full h-[600px] rounded-lg"
          frameBorder="0"
        />
      </DialogContent>
    </Dialog>
  )
}
